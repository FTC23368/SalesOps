import random
from langchain_core.messages import HumanMessage, AIMessage
from graph import SalesOpsAgent

def start_chat():
    st.title("Sales Ops Agent")
    st.header("The AI assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "thread_id" not in st.session_state:
        st.session_state.thread_id = random.randint(1000, 9999)
    thread_id = st.session_state.thread_id

    for message in st.session_state.messages:
        if message["role"] != "syste":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if prompt := st.chat_input("What's up"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

if __name__ == '__main__':
    start_chat()