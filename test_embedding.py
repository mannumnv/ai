from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

text = "I love machine learning"
vector = model.encode(text)

print("Vector size:", len(vector))
print("First 10 values:", vector[:10])