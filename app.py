from transformers import pipeline
import streamlit as st

# Load model
#chatbot = pipeline("text-generation", model="gpt2")
chatbot = pipeline("text-generation", model="distilgpt2")

st.title("AI Chatbot 🤖")

user_input = st.text_input("Ask something:")

if user_input:
    response = chatbot(user_input, max_length=100)
    st.write(response[0]['generated_text'])