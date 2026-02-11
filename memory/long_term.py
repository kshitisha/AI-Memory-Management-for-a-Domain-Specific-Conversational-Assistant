import json
import os

FILE_PATH = "data/long_term_memory.json"

def load_long_term_memory():
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        return {}
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_long_term_memory(memory: dict):
    with open(FILE_PATH, "w") as f:
        json.dump(memory, f, indent=2)
