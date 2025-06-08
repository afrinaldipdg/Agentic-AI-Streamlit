import os
from dotenv import load_dotenv # Untuk memuat variabel lingkungan dari file .env
from langchain.agents import initialize_agent, AgentType # Untuk membuat dan mengelola agen LangChain
from langchain_google_genai import ChatGoogleGenerativeAI # Untuk menggunakan model Gemini dari Google
# --- PERUBAHAN DI SINI ---
# Import alat pencarian kustom Anda yang menggunakan Tor (dikomentari)
# from ddg_tor_tool import DDGTorSearchTool
# from tools.search_tool import get_search_tool
# Tambahkan impor untuk Google Search

# Import alat lain yang masih Anda gunakan
from tools.calc_tool import get_calc_tool # Untuk alat kalkulator
from tools.memory_tool import get_memory_tool # Untuk alat memori
import streamlit as st # Untuk membangun aplikasi web interaktif

# Impor Tavily Search Tool (Alat pencarian baru)
from langchain_community.tools.tavily_search import TavilySearchResults

# --- AKHIR PERUBAHAN ---

load_dotenv() # Memuat variabel lingkungan dari file .env (misalnya, API_KEY)

@st.cache_resource # Dekorator Streamlit untuk menyimpan hasil fungsi ini agar tidak diinisialisasi ulang
def create_agent():
    # Menginisialisasi model bahasa besar (LLM) dari Google Generative AI
    # Menggunakan model "gemini-2.5-flash-preview-05-20" dengan suhu 0 (respons lebih konsisten)
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-05-20", temperature=0)

    # --- PERUBAHAN DI SINI ---
    # Inisialisasi DDGTorSearchTool (sudah dikomentari, tidak lagi digunakan)
    # Anda mungkin perlu menyesuaikan cara inisialisasinya jika ada parameter khusus
    #tor_search_tool = DDGTorSearchTool()
    # search_tool = get_search_tool() # Mengambil tool pencarian normal (sudah dikomentari)

    # Inisialisasi Tavily Search Tool
    # Pastikan TAVILY_API_KEY sudah diatur di .env Anda
    tavily_search_tool = TavilySearchResults(name="search") # Beri nama 'search' agar agen mengenalinya


    # Gabungkan alat pencarian Tor dengan alat lainnya (baris-baris ini juga dikomentari)
    # Pastikan Anda tidak lagi memanggil get_search_tool() dari tools.search_tool
    # karena itu yang bermasalah dengan koneksi langsung
    #tools = [tor_search_tool, get_calc_tool()] + get_memory_tool()
    # tools = [search_tool, get_calc_tool()] + get_memory_tool()
    #tools = [Google Search, get_calc_tool()] + get_memory_tool()

    # Gabungkan semua tools yang akan digunakan oleh agen
    # Sekarang agen akan menggunakan Tavily Search sebagai alat pencarian utamanya
    tools = [tavily_search_tool, get_calc_tool()] + get_memory_tool()
    # --- AKHIR PERUBAHAN ---

    # Menginisialisasi agen LangChain
    # tools: daftar alat yang tersedia untuk agen
    # llm: model bahasa besar yang digunakan agen untuk berpikir dan membuat keputusan
    # agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION: jenis agen yang digunakan (pola ReAct)
    # verbose=True: akan menampilkan log pemikiran agen di konsol, sangat membantu untuk debugging
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True # Ditambahkan untuk menangani kesalahan parsing
    )

    return agent
