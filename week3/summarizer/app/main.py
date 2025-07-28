# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.summarizer import summarize_text

app = FastAPI()

# Allow Streamlit frontend to access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to ["http://localhost:8501"] etc.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize(req: TextRequest):
    summary = summarize_text(req.text)
    return {"summary": summary}
