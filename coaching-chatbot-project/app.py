from flask import Flask, render_template, request, jsonify
import os
from chatbot_logic import get_bot_response

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "../templates"),
    static_folder=os.path.join(BASE_DIR, "../static")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")
        response = get_bot_response(user_message)
        return jsonify({"reply": response})
    except Exception as e:
        return jsonify({"reply": str(e)}), 500
