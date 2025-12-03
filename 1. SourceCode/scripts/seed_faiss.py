from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os
import pickle

def seed_faiss():
    # Load your initial data for seeding
    initial_data = [
        {"id": 1, "text": "Customer service is important."},
        {"id": 2, "text": "Personalization enhances user experience."},
        {"id": 3, "text": "AI can help in understanding customer needs."},
    ]

    # Create embeddings
    embeddings = OpenAIEmbeddings(model=os.getenv('EMBEDDING_MODEL'))

    # Create FAISS index
    faiss_index = FAISS(embeddings.embed_documents([item['text'] for item in initial_data]))

    # Save the FAISS index to a file
    with open('data/embeddings/faiss_index.pkl', 'wb') as f:
        pickle.dump(faiss_index, f)

if __name__ == "__main__":
    seed_faiss()