import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# 1. Load environment variables immediately
load_dotenv()

# 2. Get the API Key safely
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found in .env file!")

VECTOR_DB_PATH = "data/embeddings/faiss_index"

def build_vector_store():
    """Run this once to seed the DB"""
    print("Loading PDFs...")
    
    # Check if directory exists
    if not os.path.exists("data/knowledge_base"):
        os.makedirs("data/knowledge_base")
        print("⚠️ Created data/knowledge_base folder. Please put a PDF there!")
        return

    loader = PyPDFDirectoryLoader("data/knowledge_base")
    docs = loader.load()
    
    if not docs:
        print("⚠️ No PDFs found in data/knowledge_base/. Please add a PDF.")
        return

    print(f"Processing {len(docs)} pages...")
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    
    # PASS THE API KEY EXPLICITLY HERE
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key
    )
    
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(VECTOR_DB_PATH)
    print(f"✅ Vector Store Saved to {VECTOR_DB_PATH}!")

def get_rag_context(query_text):
    """Retrieves relevant context for a query"""
    
    # PASS THE API KEY EXPLICITLY HERE TOO
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key
    )
    
    try:
        new_db = FAISS.load_local(VECTOR_DB_PATH, embeddings, allow_dangerous_deserialization=True)
        docs = new_db.similarity_search(query_text, k=2)
        return "\n".join([d.page_content for d in docs])
    except Exception as e:
        print(f"RAG Error: {e}")
        return "No specific policy documents found."