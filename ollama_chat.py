import ollama
import os

def read_file(file_name):
    if not os.path.exists(file_name):
        return None
    with open(file_name, "r") as f:
        return f.read()

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]

while True:
    user_input = input("Mannu: ")

    if user_input.lower() == "exit":
        break

    file_data = ""
    words = user_input.split()

    # 👇 file detect
    for word in words:
        if word.endswith(".py"):
            content = read_file(word)
            if content:
                file_data += f"\n\n### File: {word}\n{content}"
            else:
                file_data += f"\n\nFile {word} not found."

    # 👇 prompt build
    if file_data:
        user_message = f"""
User asked: {user_input}

Here are the file contents:
{file_data}
"""
    else:
        user_message = user_input

    messages.append({"role": "user", "content": user_message})

    response = ollama.chat(
        model="llama3",
        messages=messages
    )

    ai_reply = response["message"]["content"]

    print("\nAI:", ai_reply, "\n")

    messages.append({"role": "assistant", "content": ai_reply})