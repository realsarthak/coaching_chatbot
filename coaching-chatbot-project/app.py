import os
import sys
from flask import Flask, render_template, request, jsonify

# Make sure Python can find chatbot_logic.py and institute_data.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from chatbot_logic import get_bot_response

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "../templates"),
    static_folder=os.path.join(BASE_DIR, "../static")
)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Chatbot API route
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(silent=True) or {}
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"reply": "Please type a question so I can help you."})

        response = get_bot_response(user_message)
        return jsonify({"reply": response})

    except Exception as e:
        return jsonify({
            "reply": "Internal server error occurred.",
            "error": str(e)
        }), 500

# Optional health check route for debugging
@app.route("/health")
def health():
    return jsonify({"status": "ok", "message": "Flask app is running successfully"})

if __name__ == "__main__":
    app.run(debug=True)
