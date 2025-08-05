import random  # Add this import
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage

def start_chat():
    st.title("SalesOps Agent")
    st.header("You AI Assistant for Sales Operations")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "thread_id" not in st.session_state:
        st.session_state.thread_id = random.randint(1000000, 9999999)
    thread_id = st.session_state.thread_id

    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if prompt := st.chat_input("What's up"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt) 

    message_history = []
    msgs = st.session_state.messages

    for m in msgs:
        if m["role"] == "user":
            message_history.append(HumanMessage(content=m["content"]))
        elif m["role"] == "assistant":
            message_history.append(AIMessage(content=m["content"]))

    app = SalesOpsAgent(st.secrets['OPENAI_API_KEY'])
    thread = {"configurable": {"thread_id": thread_id}}
    parameters = {
        "initial_message": prompt,
        "message_history": message_history,
    }



if __name__ == '__main__':
    start_chat()