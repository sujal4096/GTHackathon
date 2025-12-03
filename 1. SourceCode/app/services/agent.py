from .personalization import personalize
from .retrieval import retrieve_documents
from ..utils.logging import logger

def generate_response(data):
    user_id = data.get('user_id')
    message = data.get('message')
    lat = data.get('lat')
    lng = data.get('lng')

    logger.info(f"Received message from user {user_id}: {message}")

    context = personalize(user_id, lat, lng)
    documents = retrieve_documents(message)

    combined_input = f"{context}\n{documents}"
    response = call_gemini_llm(combined_input)
    return {"response": response}

def call_gemini_llm(input_text):
    return "This is a response from the LLM."