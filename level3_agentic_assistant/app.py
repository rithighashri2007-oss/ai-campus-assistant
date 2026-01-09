from dotenv import load_dotenv
from agent import agent_step

# load API key
load_dotenv()

print("🎓 Level 3: Agentic Campus Assistant")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("👋 Exiting...")
        break

    response = agent_step(user_input)
    print("AI:", response)
