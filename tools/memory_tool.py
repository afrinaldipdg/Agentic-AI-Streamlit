import json
from langchain_community.tools import Tool

MEMORY_FILE = "memory.json"

def save_note(note):
    try:
        with open(MEMORY_FILE, "r") as f:
            # Tambahkan penanganan JSONDecodeError di sini
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                # Jika file kosong atau tidak valid JSON, inisialisasi sebagai list kosong
                data = []
    except FileNotFoundError:
        data = [] # Jika file tidak ada, inisialisasi sebagai list kosong

    data.append(note)
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def read_notes():
    try:
        with open(MEMORY_FILE, "r") as f:
            # Tambahkan penanganan JSONDecodeError di sini juga untuk pembacaan
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return [] # Jika file kosong atau tidak valid JSON, kembalikan list kosong
    except FileNotFoundError:
        return []

def get_memory_tool():
    def save_fn(input):
        save_note(input)
        return f"Note saved: {input}"

    def read_fn(_):
        notes = read_notes()
        return "\n".join(f"- {n}" for n in notes) if notes else "No notes found."

    return [
        Tool(name="save_note", func=save_fn, description="Saves a note to memory."),
        Tool(name="read_notes", func=read_fn, description="Reads all saved notes."),
    ]
