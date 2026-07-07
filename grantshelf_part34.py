# === Stage 34: Add support for multiple local user profiles ===
# Project: GrantShelf
import os, json

class UserProfile:
    def __init__(self, name, email=None):
        self.name = name
        self.email = email
        self._path = os.path.join(os.path.expanduser("~"), ".grantshelf", f"{name}.json")
    
    @classmethod
    def load(cls):
        profiles_dir = os.path.expanduser("~/.grantshelf")
        os.makedirs(profiles_dir, exist_ok=True)
        files = [f for f in os.listdir(profiles_dir) if f.endswith(".json")]
        return {name: cls._load_json(files[0]) for name, files in [(os.path.splitext(f)[0], files)]}

    @classmethod
    def _load_json(cls, path):
        with open(path) as f:
            data = json.load(f)
        return cls(data.get("name", ""), data.get("email"))

    def save(self):
        os.makedirs(os.path.dirname(self._path), exist_ok=True)
        with open(self._path, "w") as f:
            json.dump({"name": self.name, "email": self.email}, f, indent=2)

    def __repr__(self):
        return f"<UserProfile {self.name}>"
