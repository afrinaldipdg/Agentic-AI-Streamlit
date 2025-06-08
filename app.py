import streamlit as st
from agent import create_agent

st.title("🧠 Agentic AI")

# Inisialisasi agen hanya sekali dengan st.cache_resource
# Pastikan Anda telah menambahkan @st.cache_resource di fungsi create_agent() di agent.py
agent = create_agent()

# Inisialisasi riwayat obrolan di st.session_state
# Jika 'messages' belum ada di session_state, buat list kosong.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan semua pesan dari riwayat obrolan
for message in st.session_state.messages:
    # Gunakan st.chat_message untuk tampilan chat yang lebih bagus
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Ambil input pengguna baru
# Gunakan st.chat_input untuk input chat yang lebih baik
user_input = st.chat_input("Ask something...")

if user_input:
    # Tambahkan pesan pengguna ke riwayat obrolan dan tampilkan
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Dapatkan respons dari agen
    with st.spinner("Thinking..."): # Tampilkan spinner saat agen berpikir
        response = agent.run(user_input)
    
    # Tambahkan respons agen ke riwayat obrolan dan tampilkan
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
