import ollama

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]

while True:
    user_input = input("Mannu: ")

    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    response = ollama.chat(
        model="llama3",
        messages=messages
    )

    ai_reply = response["message"]["content"]

    print("\nAI:", ai_reply, "\n")

    messages.append({"role": "assistant", "content": ai_reply})