import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv() # Memuat GOOGLE_API_KEY dari .env

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

print("Available models:")
for m in genai.list_models():
    # Periksa apakah model mendukung metode generateContent (penting untuk chat dan agen)
    if "generateContent" in m.supported_generation_methods:
        print(f"  Model Name: {m.name}, Supported Methods: {m.supported_generation_methods}")
