import streamlit as st
from agent import create_agent

# Fungsi untuk menyisipkan CSS kustom dari file style.css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Panggil fungsi untuk menyisipkan CSS
# Pastikan file style.css berada di direktori yang sama dengan app.py
local_css("style.css")

# --- Judul Aplikasi ---
st.title("Belajar Agentic AI")

# Inisialisasi agen hanya sekali dengan st.cache_resource
# Penting: Pastikan @st.cache_resource sudah ditambahkan di fungsi create_agent() di agent.py
agent = create_agent()

# Inisialisasi riwayat obrolan di st.session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan semua pesan dari riwayat obrolan
for message in st.session_state.messages:
    # Gunakan st.chat_message untuk tampilan chat yang lebih bagus
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Ambil input pengguna baru
# Gunakan st.chat_input untuk input chat yang lebih baik, biasanya di bagian bawah
user_input = st.chat_input("Tanyakan sesuatu...") # Ubah placeholder jika perlu

if user_input:
    # Tambahkan pesan pengguna ke riwayat obrolan dan tampilkan
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Dapatkan respons dari agen
    with st.spinner("Agent sedang berpikir..."): # Tampilkan spinner saat agen berpikir
        response = agent.run(user_input)
    
    # Tambahkan respons agen ke riwayat obrolan dan tampilkan
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

# --- Tambahkan Footer Bar ---
st.markdown(
    """
    <div class="footer">
        Copyright © 2025 <a href="https://github.com/afrinaldipdg" target="_blank">github.com/afrinaldipdg</a>
    </div>
    """,
    unsafe_allow_html=True,
)
