import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
# --- PERUBAHAN DI SINI ---
# Import alat pencarian kustom Anda yang menggunakan Tor
# from ddg_tor_tool import DDGTorSearchTool # Pastikan file ini ada di direktori yang sama atau dapat diakses
# from tools.search_tool import get_search_tool
# Tambahkan impor untuk Google Search

# Import alat lain yang masih Anda gunakan
from tools.calc_tool import get_calc_tool
from tools.memory_tool import get_memory_tool
import streamlit as st

# Impor Tavily Search Tool
from langchain_community.tools.tavily_search import TavilySearchResults

# --- AKHIR PERUBAHAN ---

load_dotenv()

@st.cache_resource

def create_agent():
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-preview-05-20", temperature=0)

    # --- PERUBAHAN DI SINI ---
    # Inisialisasi DDGTorSearchTool
    # Anda mungkin perlu menyesuaikan cara inisialisasinya jika ada parameter khusus
    #tor_search_tool = DDGTorSearchTool()
    # search_tool = get_search_tool() # Mengambil tool pencarian normal

    # Inisialisasi Tavily Search Tool
    # Pastikan TAVILY_API_KEY sudah diatur di .env
    tavily_search_tool = TavilySearchResults(name="search") # Beri nama 'search' agar agen mengenalinya


    # Gabungkan alat pencarian Tor dengan alat lainnya
    # Pastikan Anda tidak lagi memanggil get_search_tool() dari tools.search_tool
    # karena itu yang bermasalah dengan koneksi langsung
    #tools = [tor_search_tool, get_calc_tool()] + get_memory_tool()
    # tools = [search_tool, get_calc_tool()] + get_memory_tool()
    #tools = [Google Search, get_calc_tool()] + get_memory_tool()

    # Gabungkan semua tools
    tools = [tavily_search_tool, get_calc_tool()] + get_memory_tool()
    # --- AKHIR PERUBAHAN ---

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent
