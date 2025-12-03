# seed.py
from app.services.rag_service import build_vector_store

if __name__ == "__main__":
    print("Starting Database Seeding...")
    try:
        build_vector_store()
        print("✅ Success! Database created in 'data/embeddings/faiss_index'")
    except Exception as e:
        print(f"❌ Error: {e}")