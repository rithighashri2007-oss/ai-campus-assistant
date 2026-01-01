import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("❌ API key not found. Check your .env file.")
    exit()

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "AI Campus Assistant"
}

print("🎓 AI Campus Assistant (Level 1)")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        break

    if len(user_input) < 3:
        print("⚠️ Please ask a full question.")
        continue

    print("⏳ AI thinking...")

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=HEADERS,
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [{"role": "user", "content": user_input}],
            "max_tokens": 150,
            "temperature": 0.3
        }
    )

    if response.status_code != 200:
        print("❌ API Error:", response.text)
        continue

    data = response.json()

    if not data.get("choices"):
        print("⚠️ Model gave no answer. Try rephrasing.")
        continue

    reply = data["choices"][0]["message"]["content"].strip()

    if reply:
        print("AI:", reply)
        continue

    # Retry only if reply is empty
    print("⚠️ Retrying with simpler wording...")

    retry = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=HEADERS,
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {
                    "role": "user",
                    "content": f"Explain like teaching a 10 year old:\n{user_input}"
                }
            ],
            "max_tokens": 120,
            "temperature": 0.2
        }
    )

    retry_data = retry.json()
    if retry_data.get("choices"):
        print("AI:", retry_data["choices"][0]["message"]["content"])
