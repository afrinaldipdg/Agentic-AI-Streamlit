# 🔮 Agentic AI Streamlit

**Agentic AI Streamlit** adalah aplikasi web interaktif yang menggabungkan kekuatan agen AI otonom berbasis OpenAI (GPT-4/GPT‑4o) dengan framework LangChain, serta dukungan data dari Wikipedia dan layanan cuaca. Aplikasi ini dirancang untuk memberikan respons yang cerdas, kontekstual, dan otomatis terhadap pertanyaan pengguna melalui antarmuka berbasis Streamlit.

---

## 📌 Ringkasan Fitur

- ✅ **Agen AI Otonom** yang dapat mengambil keputusan dan melakukan tindakan.
- 🌐 **Integrasi Wikipedia** untuk menjawab pertanyaan berbasis pengetahuan umum.
- ☁️ **Tool Cuaca** untuk memberikan informasi prakiraan berdasarkan lokasi.
- 🧠 **Pemrosesan Bahasa Alami** menggunakan model GPT terkini dari OpenAI.
- 🎛️ **Antarmuka Interaktif** berbasis Streamlit yang mudah digunakan.
- 🔐 **Manajemen API Key Aman** menggunakan Streamlit Secrets.

---

## 🛠️ Instalasi dan Persiapan

### 1. Clone repositori

```bash
git clone https://github.com/afrinaldipdg/Agentic-AI-Streamlit.git
cd Agentic-AI-Streamlit

```
2. (Opsional) Aktifkan Virtual Environment

```
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

3. Install dependensi
```

pip install -r requirements.txt
```
4. Konfigurasi API Key
Buat file .streamlit/secrets.toml dan isi dengan format berikut:
```
OPENAI_API_KEY = "sk-xxxxxxx"
```
Gantilah sk-xxxxxxx dengan API key dari OpenAI milikmu.
Jika kamu menggunakan Streamlit Cloud, kamu bisa menyimpan secret ini langsung dari dashboardnya.

🚀 Menjalankan Aplikasi
Untuk menjalankan aplikasi secara lokal:

```
streamlit run app.py
```
Buka browser dan akses: http://localhost:8501

🧠 Cara Kerja Agent
Pengguna mengetik pertanyaan di antarmuka Streamlit.

Agen AI akan mengevaluasi konteks pertanyaan:

Jika perlu mencari pengetahuan umum → gunakan tool Wikipedia.

Jika terkait lokasi/cuaca → gunakan tool Cuaca.

Agen mengembalikan jawaban dalam format percakapan.

📂 Struktur Direktori
```
Agentic-AI-Streamlit/
├── app.py                  # Entry point aplikasi Streamlit
├── agent_ai.py             # Logika LangChain Agent dan Tool
├── wiki_tool.py            # Tool khusus untuk pencarian Wikipedia
├── weather_tool.py         # Tool khusus untuk informasi cuaca
├── requirements.txt        # Daftar dependensi Python
└── .streamlit/
    └── secrets.toml        # Tempat penyimpanan API key (jangan commit!)
```
🧰 Teknologi yang Digunakan
```
Teknologi	Keterangan
Python	Bahasa pemrograman utama
Streamlit	Web UI sederhana & cepat
OpenAI API	Pemrosesan bahasa alami
LangChain	Framework untuk AI agent dan tools
Wikipedia API	Sumber informasi ensiklopedia
API Cuaca	Info cuaca real-time (jika digunakan)
```
📸 Screenshot






💡 Ide Pengembangan Lanjutan
```

🔍 Integrasi dengan Google Search atau DuckDuckGo untuk hasil real-time.

💬 Chat memory agar AI mengingat konteks percakapan sebelumnya.

📁 Integrasi file upload untuk ekstraksi informasi dokumen.

🌎 Lokalisasi bahasa (multi-bahasa).

📊 Logging atau visualisasi reasoning agent secara real-time.

```

🤝 Kontribusi
Ingin berkontribusi? Mantap! Ikuti langkah berikut:

Fork repositori ini.

Buat branch baru untuk fitur atau perbaikan:

```
git checkout -b fitur-baru

```
Commit perubahanmu:

```

git commit -m "Menambahkan fitur baru"

```
Push ke branch milikmu:

```
git push origin fitur-baru

```

📄 Lisensi
Repositori ini menggunakan lisensi MIT. Silakan lihat file LICENSE untuk detail lebih lanjut.

📬 Kontak
Dikembangkan oleh Afrinaldi
Untuk pertanyaan atau kolaborasi, silakan buat issue atau hubungi melalui GitHub.

Terima kasih telah menggunakan Agentic AI Streamlit! 🌟
