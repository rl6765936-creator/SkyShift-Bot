# ==========================================
# טעינת מסמכי הידע ל-ChromaDB
# הרצה: python ingest.py   (פעם אחת, ושוב אחרי כל שינוי במסמכים)
# ==========================================
# שימוש באישורי האבטחה של Windows
# (נדרש כשסינון אינטרנט או אנטי-וירוס בודק תעבורת HTTPS)
import truststore
truststore.inject_into_ssl()

import os
import re
import time

import chromadb
from llama_index.core import Document, SimpleDirectoryReader, StorageContext, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

from config import (
    CHROMA_PATH, CHUNK_OVERLAP, CHUNK_SIZE, COLLECTION_NAME, EMBED_REQUESTS_PER_MINUTE,
    EMBEDDING_MODEL, KB_PATH,
)


def load_documents():
    """קריאת קובצי ה-Markdown והוספת מזהה מסמך וכותרת כ-Metadata."""
    documents = SimpleDirectoryReader(KB_PATH, required_exts=[".md"]).load_data()

    for doc in documents:
        doc_id = re.search(r"\*\*Document ID:\*\*\s*(\S+)", doc.text)
        title = re.search(r"^# (.+)$", doc.text, re.MULTILINE)
        doc.metadata = {
            "doc_id": doc_id.group(1) if doc_id else doc.metadata["file_name"],
            "title": title.group(1).strip() if title else doc.metadata["file_name"],
            "file_name": doc.metadata["file_name"],
        }

    return documents


def split_by_headings(documents):
    """
    שלב 1: חלוקה לפי כותרות ## (H2).
    כל סעיף נשאר שלם יחד עם תתי-הסעיפים שלו (###), כדי שלא ייווצרו קטעים זעירים.
    """
    sections = []
    for doc in documents:
        parts = re.split(r"(?m)^(?=## )", doc.text)
        # החלק שלפני הכותרת הראשונה (כותרת המסמך ופרטיו) מצורף לסעיף הראשון
        if len(parts) > 1:
            parts = [parts[0] + parts[1]] + parts[2:]

        for part in parts:
            heading = re.search(r"(?m)^## (.+)$", part)
            sections.append(Document(
                text=part.replace("\n---\n", "\n").strip(),
                metadata={**doc.metadata, "section": heading.group(1).strip() if heading else doc.metadata["title"]},
            ))
    return sections


def split_documents(documents):
    """חלוקה לפי כותרות, ואז לפי טוקנים עם חפיפה."""
    sections = split_by_headings(documents)

    # שלב 2: סעיף ארוך מ-CHUNK_SIZE נחתך לכמה קטעים עם חפיפה
    nodes = SentenceSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    ).get_nodes_from_documents(sections)

    for node in nodes:
        # שם הקובץ לא תורם לחיפוש; כותרת המסמך והסעיף כן
        node.excluded_embed_metadata_keys = ["file_name"]
        node.excluded_llm_metadata_keys = ["file_name"]

    return nodes


# התהליך המלא: טעינה, חלוקה, יצירת וקטורים ושמירה ב-ChromaDB
def main():
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("Missing GOOGLE_API_KEY")

    documents = load_documents()
    nodes = split_documents(documents)
    print(f"{len(documents)} documents -> {len(nodes)} chunks")

    # מחיקת אוסף ישן, כדי שלא יישארו קטעים כפולים
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    if COLLECTION_NAME in [c.name for c in client.list_collections()]:
        client.delete_collection(COLLECTION_NAME)
    collection = client.create_collection(COLLECTION_NAME, metadata={"hnsw:space": "cosine"})

    storage_context = StorageContext.from_defaults(
        vector_store=ChromaVectorStore(chroma_collection=collection)
    )

    embed_model = GoogleGenAIEmbedding(
        model_name=EMBEDDING_MODEL,
        embed_batch_size=20,
        retries=5,              # ניסיון חוזר אחרי שגיאת 429
        retry_max_seconds=60,
    )

    # המסלול החינמי מגביל ל-100 בקשות Embedding בדקה (כל קטע = בקשה),
    # ולכן טוענים במנות, עם המתנה של דקה בין מנה למנה
    index = VectorStoreIndex([], storage_context=storage_context, embed_model=embed_model)
    for start in range(0, len(nodes), EMBED_REQUESTS_PER_MINUTE):
        batch = nodes[start:start + EMBED_REQUESTS_PER_MINUTE]
        index.insert_nodes(batch)
        done = start + len(batch)
        print(f"Embedded {done}/{len(nodes)} chunks")
        if done < len(nodes):
            print("Waiting 60 seconds (free tier limit)...")
            time.sleep(60)

    print(f"Saved {collection.count()} chunks to ChromaDB.")


if __name__ == "__main__":
    main()
