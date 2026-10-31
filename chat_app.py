# ==========================================
# ממשק הצ'אט של SkyShift (Streamlit)
# הרצה: streamlit run chat_app.py
# ==========================================
# שימוש באישורי האבטחה של Windows
# (נדרש כשסינון אינטרנט או אנטי-וירוס בודק תעבורת HTTPS)
import os
import truststore
truststore.inject_into_ssl()

# הורדת ה-Reranker בשיטה הרגילה של Hugging Face (שרת ה-Xet החדש נחסם בסינון)
os.environ.setdefault("HF_HUB_DISABLE_XET", "1")

import re

import streamlit as st

import config
from rag import build_search_query, cited_sources, generate_answer, load_components, retrieve

st.set_page_config(page_title="SkyShift Assistant", page_icon="✈️", layout="centered")
st.title("✈️ SkyShift Assistant")
st.caption("שאלו על SkyShift - עולים לאוויר. התשובות מבוססות על מאגר הידע של המיזם בלבד.")


# טעינת המודלים והמאגר פעם אחת בלבד (ולא בכל הודעה)
@st.cache_resource
def get_components():
    return load_components()


try:
    components = get_components()
except Exception as error:
    st.error(f"שגיאה באתחול המערכת: {error}")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------- סרגל צד: מתגים ומידע ----------
with st.sidebar:
    st.subheader("הגדרות חיפוש")
    use_bm25 = st.toggle("Hybrid (BM25 + RRF)", value=config.USE_BM25)
    has_reranker = components["reranker"] is not None
    use_reranker = st.toggle("Reranker", value=config.USE_RERANKER and has_reranker, disabled=not has_reranker)
    if not has_reranker:
        st.caption("ה-Reranker כבוי (USE_RERANKER ב-config.py) או שלא נטען. החיפוש פועל בלעדיו.")
    use_rewrite = st.toggle("תרגום ושכתוב שאלה", value=config.USE_QUERY_REWRITE)
    show_debug = st.toggle("הצג שלבי חיפוש (למפתחים)", value=False)

    st.divider()
    st.write("מודלי תשובות (לפי סדר): " + ", ".join(f"`{m.model}`" for m in components["llms"]))
    st.write(f"קטעים במאגר: {components['chunk_count']}")

    if st.button("נקה שיחה", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# הסרת הסימונים [Source N] (ושורת "Sources:" אם נשארה ריקה) כשלא מציגים מקורות
def clean_answer(answer):
    if config.SHOW_SOURCES:
        return answer
    # שורה שמתחילה ב-"Sources:" או "מקורות:" נמחקת כולה
    text = re.sub(r"(?im)^\s*\**(sources|מקורות)\**\s*:.*$", "", answer)
    # כל סוגר מרובע עם Source או מקור, בכל צורה: [Source 1], [מקור 1, מקור 2]
    text = re.sub(r"[ \t]*\[[^\]]*(?:Source|מקור)[^\]]*\]", "", text)
    # שורות שנשארו רק עם פסיקים או נקודות, ורווחים מיותרים
    text = re.sub(r"(?m)^[\s,.;]*$", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# הצגת המקורות שהתשובה ציטטה בפועל, ובמצב למידה גם שאילתת החיפוש והציון של כל קטע
def show_sources(answer, documents, search_query, debug, model=None):
    cited = cited_sources(answer, documents)
    if cited and config.SHOW_SOURCES:
        with st.expander("מקורות"):
            for i, d in enumerate(documents, 1):
                if d in cited:
                    st.write(f"**[Source {i}]** {d['doc_id']} - {d['title']} - {d['section']}")
    if debug:
        with st.expander("שלבי חיפוש (ללמידה)"):
            st.write(f"שאילתת החיפוש: `{search_query}`")
            if model:
                st.write(f"המודל שענה: `{model}`")
            for i, d in enumerate(documents, 1):
                st.write(f"{i}. score={d['score']:.3f} | {d['doc_id']} | {d['section']}")
                st.caption(d["text"][:300] + "...")


# ---------- היסטוריית השיחה ----------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(clean_answer(message["content"]) if message["role"] == "assistant" else message["content"])
        if message.get("documents"):
            show_sources(message["content"], message["documents"], message["search_query"], show_debug, message.get("model"))


# ---------- שאלה חדשה ----------
question = st.chat_input("שאלו שאלה על SkyShift...")

if question:
    history = [
        {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
    ]
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("מחפש במאגר הידע..."):
            try:
                search_query = build_search_query(question, history, components["llms"], use_rewrite)
                documents = retrieve(search_query, components, use_bm25, use_reranker)
                answer, model = generate_answer(question, documents, history, components["llms"])

                st.markdown(clean_answer(answer))
                if documents:
                    show_sources(answer, documents, search_query, show_debug, model)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "documents": documents,
                    "search_query": search_query,
                    "model": model,
                })
            except Exception as error:
                st.error("אירעה שגיאה בחיפוש או ביצירת התשובה. בדקו את המפתח ואת הטרמינל.")
                print(f"Error: {error!r}")
                # הסרת השאלה שלא נענתה
                st.session_state.messages.pop()
