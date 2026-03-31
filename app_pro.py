import streamlit as st
from transformers import pipeline

# Load model (lightweight)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="sshleifer/tiny-gpt2")

chatbot = load_model()

# UI
st.set_page_config(page_title="AI Chatbot Pro", layout="centered")
st.title("🤖 AI Chatbot Pro")

# Initialize memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # context memory
    context = ""
    for msg in st.session_state.messages[-5:]:
        context += f"{msg['role']}: {msg['content']}\n"

    response = chatbot(
        context,
        max_length=150,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.9,
        repetition_penalty=1.2
    )

    bot_reply = response[0]["generated_text"].replace(context, "").strip()

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.write(bot_reply)