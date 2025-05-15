from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages
    )

    reply = response.choices[0].message.content
    return jsonify({"reply": reply})
