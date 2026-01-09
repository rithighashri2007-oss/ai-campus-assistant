# ================================
# LEVEL 3: AGENTIC AI - agent.py
# ================================

import os
import requests
from dotenv import load_dotenv

from memory import Memory
from tools import search_knowledge

# -------- LOAD ENV --------
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY not found in .env")

# -------- INIT MEMORY --------
memory = Memory()

# ================================
# LLM CALL
# ================================
def call_llm(user_prompt):
    memory_context = memory.get()

    full_prompt = f"""
You are an Agentic AI Campus Assistant.

Memory:
{memory_context}

User Query:
{user_prompt}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": [{"role": "user", "content": full_prompt}],
            "temperature": 0.3
        }
    )

    return response.json()["choices"][0]["message"]["content"]


# ================================
# AGENT STEP (BRAIN)
# ================================
def agent_step(user_input):
    user_input_lower = user_input.lower()

    # -------- STORE NAME --------
    if user_input_lower.startswith("my name is"):
        name = user_input.split("is", 1)[1].strip()
        memory.add(f"User name is {name}")
        return f"Nice to meet you, {name}! 😊"

    # -------- STORE YEAR --------
    if "1st year" in user_input_lower or "first year" in user_input_lower:
        memory.add("User is a 1st year college student")
        return "Got it 👍 I’ll remember that you are a 1st year student."

    # -------- RETRIEVE MEMORY --------
    if any(phrase in user_input_lower for phrase in [
        "what is my name",
        "do you remember my name",
        "do u remember my name",
        "what do you remember about me"
    ]):
        mem = memory.get()
        if mem:
            return f"📌 I remember:\n{mem}"
        else:
            return "❌ I don't remember anything yet."

    # -------- TOOL USAGE --------
    if any(word in user_input_lower for word in [
          "library",
        "college",
        "campus",
        "timing",
        "family",
        "parents",
        "father",
        "mother",
        "sister",
        "friends",
        "gpa",
        "education"
    ]):

        results = search_knowledge(user_input)
        tool_data = "\n".join(results)

        prompt = f"""
Use the following information to answer the question.

Information:
{tool_data}

Question:
{user_input}

If the answer is not found in the information, say "I don't know".
"""
        return call_llm(prompt)

    # -------- DEFAULT LLM --------
    return call_llm(user_input)
