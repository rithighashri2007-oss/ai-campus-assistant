import os
import requests
import math
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
if not API_KEY:
    print("❌ API key missing")
    exit()

# ---------------------------
# EMBEDDING FUNCTION
# ---------------------------
def embed(text):
    r = requests.post(
        "https://openrouter.ai/api/v1/embeddings",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "AI Campus Assistant"
        },
        json={
            "model": "text-embedding-3-small",
            "input": text
        }
    )
    r.raise_for_status()
    return r.json()["data"][0]["embedding"]

# ---------------------------
# COSINE SIMILARITY
# ---------------------------
def cosine(a, b):
    dot = sum(x*y for x, y in zip(a, b))
    mag_a = math.sqrt(sum(x*x for x in a))
    mag_b = math.sqrt(sum(x*x for x in b))
    return dot / (mag_a * mag_b)

# ---------------------------
# LOAD FAMILY DATA
# ---------------------------
DATA_PATH = "data/family_data.txt"
with open(DATA_PATH, "r", encoding="utf-8") as f:
    docs = [line.strip() for line in f if line.strip()]
print(f"🔹 Loaded {len(docs)} chunks from {DATA_PATH}")
# ---------------------------
# GENERATE DOCUMENT EMBEDDINGS
# ---------------------------
doc_vectors = []
for i, d in enumerate(docs, 1):
	doc_vectors.append(embed(d))
	
print("🎓 AI Campus Assistant – Level 2")
print("Type 'exit' to quit\n")

# ---------------------------
# CHAT LOOP
# ---------------------------
while True:
    question = input("You: ").strip()
    if question.lower() == "exit":
        break

    q_vec = embed(question)

    # ---------------------------
    # TOP-N chunk retrieval
    # ---------------------------
    scores = [cosine(q_vec, dv) for dv in doc_vectors]
    top_n = 5  # or 4 for small documents
    scores_with_index = list(enumerate(scores))
    scores_with_index.sort(key=lambda x: x[1], reverse=True)
    top_chunks = [docs[i] for i, s in scores_with_index[:top_n]]
    context = "\n".join(top_chunks)

    prompt = f"""
Use ONLY this information to answer.

Context:
{context}

Question:
{question}

If answer not in context, say "I don't know".
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2
        }
    )

    print("AI:", response.json()["choices"][0]["message"]["content"])
