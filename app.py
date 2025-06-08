import streamlit as st
from agent import create_agent

st.title("🧠 Agentic AI")
agent = create_agent()

user_input = st.text_input("Ask something...")

if user_input:
    response = agent.run(user_input)
    st.write("🤖", response)

