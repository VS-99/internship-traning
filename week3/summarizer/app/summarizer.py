# app/summarizer.py

import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable
from langchain_community.chat_models import ChatOpenAI

load_dotenv()

# Use OpenRouter-compatible endpoint for Mistral or OpenChat
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",  # You can also try: openchat/openchat-3.5
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# Prompt template
prompt = PromptTemplate.from_template(
    "Summarize the following text in 3-5 bullet points:\n\n{input_text}"
)

# Summarization chain
chain: Runnable = prompt | llm | StrOutputParser()

def summarize_text(text: str) -> str:
    try:
        result = chain.invoke({"input_text": text})
        return result
    except Exception as e:
        return f"Error: {e}"
