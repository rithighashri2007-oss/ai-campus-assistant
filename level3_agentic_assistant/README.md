Subject: Level 3: Agentic AI Campus Assistant



\# Level 3 – Agentic AI Campus Assistant



\## Overview



This project demonstrates \*\*Agentic AI\*\*, where the AI system does not just answer queries but \*\*decides actions\*\*, uses \*\*tools\*\*, and maintains \*\*memory\*\*.



Unlike traditional chatbots, this assistant:



\* Decides \*what to do\* before responding

\* Uses different tools based on intent

\* Remembers user-provided information

\* Acts autonomously without external frameworks



---



\## What is Agentic AI?



Agentic AI refers to systems that:



\* Observe user input

\* Decide next actions

\* Execute tools

\* Maintain internal memory

\* Loop until a goal is achieved



This project implements agentic behavior \*\*from scratch\*\* without LangChain.



---



\## Agent Components



\### 1. Decision Maker (Agent Brain)



The function `agent\_decide()` determines:



\* Whether to store memory

\* Whether to search data

\* Whether to directly call the LLM



\### 2. Tools



\* `search\_data()` → searches campus data

\* `save\_memory()` → stores long-term memory

\* `read\_memory()` → retrieves memory



\### 3. Memory



\* Stored in `memory.txt`

\* Persists across conversations



\### 4. LLM



\* Powered by OpenRouter (Mistral-7B)

\* Used only when reasoning is needed



---



\## Example Interactions



```

Remember my name is Rithigha

What is my name?

What are library timings?

```



---



\## Why No LangChain?



This project intentionally avoids frameworks to:



\* Clearly demonstrate agent logic

\* Improve understanding of agent internals

\* Reduce system overhead

\* Ensure compatibility with low-end systems



---



\## How to Run



```bash

pip install -r requirements.txt

python app.py

```



---



\## Author



Rithigha

AI Campus Assistant – Level 3



