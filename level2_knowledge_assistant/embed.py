import os
import sys
import requests
import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv

print("🔹 Starting embedding process...")

# -------------------------
# ENV
# -------------------------
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("❌ API key missing")
    sys.exit(1)

# -------------------------
# PATHS
# -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_db")
# -------------------------
# -------------------------
# -------------------------
# -------------------------
# change the data path according to the file here,downnnnnnnnnnnnnnnnnnnnn
DATA_PATH = os.path.join(BASE_DIR, "data", "family_data.txt")#hereeeeeeeeeeeeee
#========================================================================
print("📂 Chroma path:", CHROMA_PATH)
print("📄 Data file:", DATA_PATH)

# -------------------------
# READ DATA
# -------------------------
with open(DATA_PATH, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

print(f"🔹 Total chunks: {len(lines)}")

# -------------------------
# CHROMA (telemetry OFF)
# -------------------------
client = chromadb.Client(
    Settings(
        persist_directory=CHROMA_PATH,
        anonymized_telemetry=False
    )
)

collection = client.get_or_create_collection(
    name="campus_knowledge"
)

# -------------------------
# EMBEDDING
# -------------------------
def embed_text(text):
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
        },
        timeout=60
    )
    r.raise_for_status()
    return r.json()["data"][0]["embedding"]

embeddings = []

for i, line in enumerate(lines):
    print(f"🔹 Embedding chunk {i+1}/{len(lines)}")
    embeddings.append(embed_text(line))

print("📥 Adding vectors to ChromaDB...")

collection.add(
    documents=lines,
    embeddings=embeddings,
    ids=[f"doc_{i}" for i in range(len(lines))]
)

print("💾 Persisting to disk...")
client.persist()

print("📊 Vector count:", collection.count())

print("✅ EMBEDDING SUCCESSFUL")
print("📁 chroma_db exists:", os.path.exists(CHROMA_PATH))

# 🔴 THIS LINE IS CRITICAL ON WINDOWS
client._system.stop()

print("🏁 Done.")


