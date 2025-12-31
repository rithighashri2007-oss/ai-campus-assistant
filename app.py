
import requests
import time
API_KEY = "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"


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
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {
                    "role": "user",
                    "content": f"Answer clearly in simple English:\n{user_input}"
                }
            ],
            "max_tokens": 150,
            "temperature": 0.3
        }
    )

    if response.status_code != 200:
        print("❌ API Error:", response.text)
        continue

    data = response.json()

    if "choices" not in data or len(data["choices"]) == 0:
        print("⚠️ Model gave no answer. Try rephrasing.")
        continue

    reply = data["choices"][0]["message"]["content"].strip()

    if reply == "":
    print("⚠️ Retrying with simpler wording...")

    retry = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {
                    "role": "user",
                    "content": f"Explain chemistry like teaching a 10 year old:\n{user_input}"
                }
            ],
            "max_tokens": 120,
            "temperature": 0.2
        }
    )

    retry_data = retry.json()
    if "choices" in retry_data and retry_data["choices"]:
        print("AI:", retry_data["choices"][0]["message"]["content"])
    continue
