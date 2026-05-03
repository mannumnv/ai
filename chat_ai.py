from sentence_transformers import SentenceTransformer, util

# -----------------------------
# 1. Load AI embedding model
# -----------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')

# -----------------------------
# 2. Memory (like ChatGPT context DB)
# -----------------------------
memory = [
    "My name is Manmohan",
    "I am an AI assistant",
    "I help answer questions",
    "You can ask me anything",
    "I was built using embeddings",
]

# Pre-compute embeddings
memory_embeddings = model.encode(memory)

# -----------------------------
# 3. Chat function (core logic)
# -----------------------------
def chat(query):
    query_embedding = model.encode(query)

    scores = util.cos_sim(query_embedding, memory_embeddings)[0]

    best_idx = scores.argmax()
    best_score = scores[best_idx].item()

    # ⚠️ threshold fix
    if best_score < 0.4:
        return "Sorry, I don't know about that.", best_score

    return memory[best_idx], best_score


# -----------------------------
# 4. Interactive chat loop
# -----------------------------
print("\n🤖 AI Chat System Ready (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    answer, score = chat(user_input)

    print(f"\nAI: {answer}")
    print(f"(confidence: {round(score, 3)})\n")