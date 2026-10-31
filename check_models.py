# ==========================================
# בדיקה שמזהי המודלים זמינים במפתח שלכם
# הרצה: python check_models.py
# ==========================================
# שימוש באישורי האבטחה של Windows
# (נדרש כשסינון אינטרנט או אנטי-וירוס בודק תעבורת HTTPS)
import truststore
truststore.inject_into_ssl()

import os
import sys

from google import genai

from config import CHAT_MODELS, EMBEDDING_MODEL


# מציג אילו מודלים זמינים למפתח ושולח בקשת בדיקה קטנה לכל מודל שבחרנו
def main():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        sys.exit("Missing GOOGLE_API_KEY. In PowerShell: $env:GOOGLE_API_KEY=\"...\"")

    client = genai.Client(api_key=api_key)

    # 1. רשימת המודלים שהמפתח רואה
    names = [m.name.removeprefix("models/") for m in client.models.list()]
    print("Flash models available to your key:")
    for name in sorted(n for n in names if "flash" in n):
        print("  ", name)
    print("Embedding models available to your key:")
    for name in sorted(n for n in names if "embedding" in n):
        print("  ", name)

    ok = True

    # 2. בדיקת מודלי התשובות. מספיק שאחד מהם עובד, כי הבוט עובר ביניהם לבד
    print()
    working = 0
    for model in CHAT_MODELS:
        try:
            reply = client.models.generate_content(model=model, contents="Reply with the word OK.")
            print(f"[OK] {model}: {reply.text.strip()}")
            working += 1
        except Exception as error:
            print(f"[FAIL] {model}: {str(error)[:150]}")
    if working == 0:
        ok = False

    # 3. בדיקת מודל ה-Embeddings
    try:
        result = client.models.embed_content(model=EMBEDDING_MODEL, contents="SkyShift test")
        print(f"[OK] {EMBEDDING_MODEL}: vector length {len(result.embeddings[0].values)}")
    except Exception as error:
        ok = False
        print(f"[FAIL] {EMBEDDING_MODEL}: {error}")

    if ok:
        print("\nAll models work. Next step: python ingest.py")
    else:
        print("\nPick a model from the lists above and update config.py, then run this again.")


if __name__ == "__main__":
    main()
