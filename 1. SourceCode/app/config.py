import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    EMBEDDING_MODEL = os.getenv('EMBEDDING_MODEL', 'text-embedding-004')
    LLM_MODEL = os.getenv('LLM_MODEL', 'gemini-pro')