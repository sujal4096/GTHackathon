from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Import services
from app.services.llm_agent import get_ai_response, generate_welcome_message

load_dotenv()

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start_chat():
    user_id = request.json.get("user_id", "u123")
    welcome_msg = generate_welcome_message(user_id)
    return jsonify({"response": welcome_msg})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")
    user_id = data.get("user_id", "u123")
    
    try:
        response_text = get_ai_response(user_id, user_message)
        return jsonify({"response": response_text})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": "I'm having trouble connecting right now."}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)