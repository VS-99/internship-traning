from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load trained model
model = joblib.load("models/sentiment_model.pkl")

# Initialize FastAPI app
app = FastAPI(title="Sentiment Analyzer API")

# Request body schema
class SentimentRequest(BaseModel):
    text: str

# Home route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentiment Analyzer API"}

# Prediction route
@app.post("/predict")
def predict_sentiment(req: SentimentRequest):
    prediction = model.predict([req.text])[0]
    return {
        "input": req.text,
        "sentiment": prediction
    }
