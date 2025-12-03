import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
# REMOVED: from langchain.memory import ConversationBufferMemory (Causing Error)
from app.utils.pii_masker import mask_sensitive_data
from app.services.rag_service import get_rag_context

load_dotenv()

# --- 1. SIMPLE CUSTOM MEMORY (No Libraries) ---
# Format: { "u123": "User: Hi\nAI: Hello\n..." }
chat_histories = {}

def get_history(user_id):
    return chat_histories.get(user_id, "")

def update_history(user_id, user_msg, ai_msg):
    current = chat_histories.get(user_id, "")
    # Append new interaction
    new_entry = f"User: {user_msg}\nAI: {ai_msg}\n"
    chat_histories[user_id] = current + new_entry

# --- 2. DATA LOADING ---
try:
    users = json.load(open('data/users.json'))
    stores = json.load(open('data/stores.json'))
except:
    users, stores = {}, []

# --- 3. DYNAMIC GREETING GENERATOR ---
def generate_welcome_message(user_id):
    user = users.get(user_id, {"name": "Guest"})
    store = stores[0] if stores else {"name": "Generic Store", "promotions": []}
    
    # Use API Key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key: return "Welcome! (API Key Missing)"
    
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
    
    prompt = f"""
    You are a helpful Retail Assistant. 
    User Name: {user.get('name')}
    Nearby Store: {store.get('name')}
    Current Promos: {', '.join(store.get('promotions', []))}
    
    Task: Write a short, punchy, 1-sentence welcome message inviting them in. 
    Mention a specific promo if available. Use an emoji.
    """
    try:
        response = llm.invoke(prompt)
        return response.content
    except:
        return "Welcome to our store! We have great offers today."

# --- 4. MAIN CHAT AGENT ---
def get_ai_response(user_id, raw_message):
    clean_message = mask_sensitive_data(raw_message)
    
    # Get Context
    user_profile = users.get(user_id, {})
    nearby_store = stores[0] if stores else "Unknown"
    
    # Get Manual History
    history_text = get_history(user_id)

    # Get RAG
    rag_info = get_rag_context(clean_message)

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key: return "System Error: API Key missing."
    
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)

    template = """
    You are a Hyper-Personalized Retail Assistant.
    
    USER PROFILE: {user_profile}
    NEARBY STORE: {store_info}
    
    PREVIOUS CONVERSATION:
    {history}
    
    KNOWLEDGE BASE (RAG):
    {rag_data}
    
    CURRENT USER INPUT: {user_message}
    
    GUIDELINES:
    1. Be concise and friendly.
    2. Use Markdown for formatting (e.g., **bold** for offers).
    3. If recommending a product, mention the specific price or discount.
    4. Use the PREVIOUS CONVERSATION to answer follow-up questions.
    """
    
    prompt = PromptTemplate(
        input_variables=["user_profile", "store_info", "history", "rag_data", "user_message"],
        template=template
    )

    final_prompt = prompt.format(
        user_profile=str(user_profile),
        store_info=str(nearby_store),
        history=history_text,
        rag_data=rag_info,
        user_message=clean_message
    )

    try:
        response = llm.invoke(final_prompt)
        ai_text = response.content
        
        # Save to Manual History
        update_history(user_id, clean_message, ai_text)
        
        return ai_text
    except Exception as e:
        return f"System Error: {str(e)}"