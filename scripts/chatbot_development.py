# Script to develop the chatbot interface
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
chatbot = pipeline('conversational', model='microsoft/DialoGPT-medium')

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chatbot(user_input)
    return jsonify({"response": response[0]["generated_text"]})

if __name__ == "__main__":
    app.run(debug=True)
