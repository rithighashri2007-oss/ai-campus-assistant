import os
import requests
import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv

print("🔹 Starting embedding process...")

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
if not API_KEY:
    print("❌ API key missing")
    exit()

# -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_db")
DATA_PATH = os.path.join(BASE_DIR, "data", "family_data.txt")

print("📂 Chroma path:", CHROMA_PATH)
print("📄 Data file:", DATA_PATH)

# -------------------------
with open(DATA_PATH, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

print(f"🔹 Total chunks: {len(lines)}")

# -------------------------
client = chromadb.Client(
    Settings(
        persist_directory=CHROMA_PATH,  # important for Windows
        anonymized_telemetry=False
    )
)

collection_name = "family_knowledge"
if collection_name in [c.name for c in client.list_collections()]:
    collection = client.get_collection(collection_name)
else:
    collection = client.create_collection(name=collection_name)

# -------------------------
def embed_text(text):
    r = requests.post(
        "https://openrouter.ai/api/v1/embeddings",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={"model": "text-embedding-3-small", "input": text},
        timeout=60
    )
    r.raise_for_status()
    return r.json()["data"][0]["embedding"]

embeddings = []
for i, line in enumerate(lines):
    print(f"🔹 Embedding chunk {i+1}/{len(lines)}")
    embeddings.append(embed_text(line))

# -------------------------
print("📥 Adding vectors to ChromaDB...")
collection.add(
    documents=lines,
    embeddings=embeddings,
    ids=[f"doc_{i}" for i in range(len(lines))]
)

# Persist safely
client.persist()
print("💾 ChromaDB persisted successfully")
print("📊 Vector count:", collection.count())

