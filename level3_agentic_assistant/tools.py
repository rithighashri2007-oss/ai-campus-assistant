import os

DATA_PATH = "data"

STOP_WORDS = {
    "tell", "me", "about", "my", "is", "the", "a", "an",
    "what", "who", "where", "when", "do", "does", "are"
}

def search_knowledge(query):
    results = []

    # remove useless words
    query_words = [
        word for word in query.lower().split()
        if word not in STOP_WORDS
    ]

    if not os.path.exists(DATA_PATH):
        return ["Data folder not found"]

    for file in os.listdir(DATA_PATH):
        if file.endswith(".txt"):
            with open(os.path.join(DATA_PATH, file), "r", encoding="utf-8") as f:
                for line in f:
                    line_lower = line.lower()
                    if any(word in line_lower for word in query_words):
                        results.append(line.strip())
    return results if results else ["No relevant data found"]

    