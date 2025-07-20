import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
import os

# Load dataset
df = pd.read_csv("data/sentiment.csv")

# Build and train pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(df["text"], df["label"])

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/sentiment_model.pkl")
print("✅ Model trained and saved at models/sentiment_model.pkl")
