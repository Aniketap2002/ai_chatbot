import streamlit as st
import requests

# Page title
st.title("HI Aniket. \n How is your day today🤖")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Send request to FastAPI
    response = requests.get(
        "http://127.0.0.1:8000/chat",
        params={"query": user_input}
    )

    ai_response = response.json()["response"]

    # Show AI response
    with st.chat_message("assistant"):
        st.write(ai_response)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })