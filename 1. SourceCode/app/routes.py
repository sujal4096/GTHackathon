from flask import jsonify, request
from .services.agent import generate_response

def register_routes(app):
    @app.route('/health', methods=['GET'])
    def health():
        return jsonify({"status": "healthy"}), 200

    @app.route('/chat', methods=['POST'])
    def chat():
        data = request.json
        response = generate_response(data)
        return jsonify(response), 200