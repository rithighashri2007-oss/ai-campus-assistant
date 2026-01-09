# AI Campus Assistant

A **multi-level AI Campus Assistant** project built step‑by‑step to demonstrate the evolution from a basic chatbot to an **Agentic AI system with memory and tool usage**.

This project was developed as part of a **Tech Club AI Task**, focusing on clean architecture, modular design, and real‑world AI agent concepts.

## 📂 Project Structure

ai-campus-assistant/
│
├── level1_basic_assistant/
│   ├── app.py
│   ├── README.md
│   └── .gitignore
│
├── level2_knowledge_assistant/
│   ├── app.py
│   ├── embed.py
│   ├── data/
│   ├── README.md
│   └── .gitignore
│
├── level3_agentic_assistant/
│   ├── app.py
│   ├── agent.py
│   ├── tools.py
│   ├── memory.py
│   ├── data/
│   ├── README.md
│   └── .gitignore
│
├── .gitignore
└── README.md

##  Level Overviews....

### Level 1 – Basic AI Assistant

* Simple conversational AI
* Handles basic user inputs
* No memory or external knowledge

**Goal:** Understand LLM API usage and basic chatbot flow.

### 🔹 Level 2 – Knowledge‑Based Assistant

* Uses external **text files** as a knowledge source
* Searches data from `data/` folder
* Answers campus‑related queries (library, timings, departments)

**Goal:** Introduce retrieval‑based question answering.

### 🔹 Level 3 – Agentic AI Assistant (Advanced)

This is the **core highlight** of the project.

**Features:**

*  Memory system (stores user info like name, year, GPA)
*  Tool usage (searches multiple `.txt` knowledge files)
*  Decision‑making agent (decides when to use memory, tools, or LLM)
*  Supports multiple domains (campus data + family data)

**Key Components:**

* `agent.py` → Agent brain & decision logic
* `memory.py` → Short‑term memory buffer
* `tools.py` → Knowledge search tool
* `data/` → Campus & family information files

**Goal:** Build a real Agentic AI system.

##  Technologies Used

* Python
* OpenRouter API (LLM)
* Requests
* dotenv
* Git & GitHub

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/ai-campus-assistant.git
cd ai-campus-assistant
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variables

Create a `.env` file inside each level folder:

```
OPENROUTER_API_KEY=your_api_key_here
```

---

## ▶️ How to Run

### Level 1

```bash
cd level1_basic_assistant
python app.py
```

### Level 2

```bash
cd level2_knowledge_assistant
python app.py
```

### Level 3

```bash
cd level3_agentic_assistant
python app.py
```


## 💡 Example Questions

**Memory‑based:**

* What is my name?
* What is my GPA?

**Campus‑based:**

* Where is the library?
* What are the college timings?

**Family‑based:**

* Who is my father?
* What does my mother do?

---

## 🧠 Learning Outcomes

* Understanding AI agent architecture
* Tool‑augmented LLMs
* Memory handling in conversational AI
* Clean modular Python design
* Real‑world debugging & error handling

---

## 📌 Future Improvements

* Long‑term memory (vector DB)
* Multi‑agent collaboration
* Web interface (React / Streamlit)
* Role‑based agents (Student, Admin, Faculty)

---

## 👤 Author

**Rithigha**
First‑year student | AI & Tech Club Enthusiast

---

⭐ If you find this project useful, feel free to star the repository!
