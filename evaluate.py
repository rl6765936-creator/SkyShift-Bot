# ==========================================
# בדיקה: האם Hybrid ו-Reranker באמת משפרים את החיפוש?
# הרצה: python evaluate.py
#
# המדדים:
#   Hit@K - בכמה שאלות הקטע הנכון הגיע ל-K הקטעים שנשלחים ל-Gemini
#   MRR   - כמה גבוה הקטע הנכון בדירוג (1.0 = תמיד ראשון)
# בסוף מוצגים ציוני ה-Reranker לשאלות רלוונטיות מול לא רלוונטיות,
# כדי לבחור סף רלוונטיות על סמך נתונים ולא באופן שרירותי.
# ==========================================
# שימוש באישורי האבטחה של Windows
# (נדרש כשסינון אינטרנט או אנטי-וירוס בודק תעבורת HTTPS)
import os
import truststore
truststore.inject_into_ssl()

# הורדת ה-Reranker בשיטה הרגילה של Hugging Face (שרת ה-Xet החדש נחסם בסינון)
os.environ.setdefault("HF_HUB_DISABLE_XET", "1")

import json

import config
from rag import build_search_query, load_components


# קטע נחשב נכון אם הוא מהמסמך הצפוי ומכיל את הביטוי הצפוי
def is_correct(node, item):
    return (
        node.metadata.get("doc_id") == item["doc_id"]
        and item["must_contain"].lower() in node.get_content().lower()
    )


def score_ranking(nodes, item):
    """מחזיר (hit, reciprocal_rank) לפי K הקטעים הראשונים."""
    for rank, r in enumerate(nodes[: config.FINAL_TOP_K], 1):
        if is_correct(r.node, item):
            return 1, 1 / rank
    return 0, 0.0


# מריץ את כל שאלות הבדיקה בארבע ההגדרות ומדפיס טבלת השוואה
def main():
    with open("eval_questions.json", encoding="utf-8") as f:
        data = json.load(f)

    c = load_components()
    has_reranker = c["reranker"] is not None
    setups = ["vector", "hybrid"] + (["vector+rerank", "hybrid+rerank"] if has_reranker else [])
    if not has_reranker:
        print("Reranker not available: comparing vector vs hybrid only.\n")
    totals = {s: [0, 0.0] for s in setups}
    relevant_scores = []

    for item in data["in_scope"]:
        # שאילתת החיפוש מחושבת פעם אחת ומשמשת את כל ההגדרות
        query = build_search_query(item["question"], [], c["llms"])

        # המועמדים נשלפים פעם אחת לכל שיטה; ה-Rerank רץ מקומית
        candidates = {
            "vector": c["vector"].retrieve(query),
            "hybrid": c["hybrid"].retrieve(query),
        }
        rankings = {"vector": candidates["vector"], "hybrid": candidates["hybrid"]}
        if has_reranker:
            rankings["vector+rerank"] = c["reranker"].postprocess_nodes(candidates["vector"], query_str=query)
            rankings["hybrid+rerank"] = c["reranker"].postprocess_nodes(candidates["hybrid"], query_str=query)

        marks = []
        for s in setups:
            hit, rr = score_ranking(rankings[s], item)
            totals[s][0] += hit
            totals[s][1] += rr
            marks.append("✔" if hit else "✘")

        top = rankings.get("hybrid+rerank")
        if top and is_correct(top[0].node, item):
            relevant_scores.append(top[0].score)

        print(f"{' '.join(marks)}  {item['question']}  ->  {query}")

    n = len(data["in_scope"])
    print(f"\n{'setup':<16}{'Hit@' + str(config.FINAL_TOP_K):<10}MRR")
    for s in setups:
        hits, rr = totals[s]
        print(f"{s:<16}{hits}/{n:<8}{rr / n:.3f}")

    if not has_reranker:
        return

    # ציוני Reranker לשאלות שאין להן תשובה במאגר
    print("\nTop reranker score for out-of-scope questions:")
    unrelated_scores = []
    for question in data["out_of_scope"]:
        query = build_search_query(question, [], c["llms"])
        top = c["reranker"].postprocess_nodes(c["hybrid"].retrieve(query), query_str=query)
        score = top[0].score if top else float("-inf")
        unrelated_scores.append(score)
        print(f"  {score:8.3f}  {question}")

    if relevant_scores:
        print(f"\nLowest top score among correctly answered questions: {min(relevant_scores):.3f}")
    print(f"Highest top score among out-of-scope questions:      {max(unrelated_scores):.3f}")
    print("A threshold is useful only if it sits between these two numbers.")


if __name__ == "__main__":
    main()
