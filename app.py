from transformers import pipeline
import streamlit as st


@st.cache_resource
def load_model():
    return pipeline("text-generation", model="distilgpt2")

chatbot = load_model()

st.title("AI Chatbot 🤖")

user_input = st.text_input("Ask something:")

if user_input:
    #response = chatbot(user_input, max_length=100)
    response = chatbot(
    user_input,
    max_length=100,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    top_p=0.9,
    repetition_penalty=1.2
)
    st.write(response[0]['generated_text'].replace(user_input, ""))

    #st.write(response[0]['generated_text'])


# Load model
#chatbot = pipeline("text-generation"""  """", model="gpt2")
# chatbot = pipeline("text-generation", model="distilgpt2")

# st.title("AI Chatbot 🤖")

# user_input = st.text_input("Ask something:")

# if user_input:
#     response = chatbot(user_input, max_length=100)
#     st.write(response[0]['generated_text'])