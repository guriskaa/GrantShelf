# === Stage 13: Add file save support using a configurable path ===
# Project: GrantShelf
import os, json
from pathlib import Path

class GrantShelfConfig:
    def __init__(self):
        self.base_path = Path.home() / ".grantshelf"
        self.data_file = self.base_path / "data.json"
        self._ensure_dir()

    def _ensure_dir(self):
        self.base_path.mkdir(parents=True, exist_ok=True)

    def save_state(self, state: dict) -> bool:
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(state, f, indent=2, ensure_ascii=False)
            return True
        except Exception:
            print("Failed to save data.")
            return False

    def load_state(self) -> dict | None:
        if not self.data_file.exists():
            return {}
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            print("Failed to load data.")
            return {}

    def get_path(self) -> Path:
        return self.base_path
