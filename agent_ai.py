import ollama
from tools import run_command

SYSTEM_PROMPT = """
You are an AI DevOps assistant.
If user asks to push code, generate proper git commands.
Only output command, nothing else.
"""

def ask_ai(user_input):
    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )
    return response["message"]["content"]

while True:
    user = input("Mannu: ")

    if user == "exit":
        break

    ai_response = ask_ai(user)
    print("\nAI Suggestion:\n", ai_response)

    confirm = input("\nRun this command? (y/n): ")

    if confirm == "y":
        output = run_command(ai_response)
        print("\nResult:\n", output)