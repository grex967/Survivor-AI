from transformers import pipeline

# Force CPU use since GPU is overloaded
survivor = pipeline(
    "text-generation",
    model="C:/Users/Owner/survivor/models/survivor_model",
    tokenizer="C:/Users/Owner/survivor/models/survivor_model",
    device=-1
)

question = "How do I survive a snake bite in the wild?"
response = survivor(question, max_new_tokens=100)[0]["generated_text"]

print("\n🧠 Survivor AI says:\n", response)
