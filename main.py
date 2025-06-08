from agent import create_agent

def main():
    print("🤖 Welcome to your Agentic AI (type 'exit' to quit)")
    agent = create_agent()

    while True:
        user_input = input("\n🧠 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        response = agent.run(user_input)
        print(f"\n🤖 Agent: {response}")

if __name__ == "__main__":
    main()

