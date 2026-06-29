# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: GrantShelf
import json
from pathlib import Path

def load_grant_data(file_path: str) -> dict | None:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            print("Error: JSON root must be an object.")
            return None
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Malformed JSON in '{file_path}': {e}")
        return None
