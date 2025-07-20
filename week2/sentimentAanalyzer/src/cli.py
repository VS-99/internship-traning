import joblib

# Load model
model = joblib.load("models/sentiment_model.pkl")

# User input loop
print("🧠 Sentiment Analyzer CLI")
print("Type 'exit' to quit.\n")

while True:
    text = input("Enter text: ")
    if text.lower() == "exit":
        break
    prediction = model.predict([text])[0]
    print(f"Sentiment: {prediction}\n")
