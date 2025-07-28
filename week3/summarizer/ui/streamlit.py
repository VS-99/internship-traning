# ui/streamlit_app.py

import streamlit as st
import requests

API_URL = "http://localhost:8000/summarize"  # Change if deployed

st.set_page_config(page_title="SmartSummarizer AI", layout="centered")
st.title("🧠 SmartSummarizer AI")
st.markdown("Summarize long text using Mistral 7B via OpenRouter (LangChain API).")

text = st.text_area("Paste your text below:", height=300)

if st.button("Summarize"):
    if text.strip():
        with st.spinner("Calling FastAPI server..."):
            try:
                res = requests.post(API_URL, json={"text": text})
                if res.status_code == 200:
                    st.success(res.json()["summary"])
                else:
                    st.error("Error from server.")
            except Exception as e:
                st.error(f"Request failed: {e}")
    else:
        st.warning("Please enter some text.")
