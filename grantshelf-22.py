# === Stage 22: Add favorite records and quick favorite listing ===
# Project: GrantShelf
class GrantShelf:
    def __init__(self):
        self._favorites = set()
    
    def toggle_favorite(self, record_id: str) -> None:
        if record_id in self._favorites:
            self._favorites.remove(record_id)
        else:
            self._favorites.add(record_id)
    
    def is_favorite(self, record_id: str) -> bool:
        return record_id in self._favorites
    
    def get_favorites(self) -> list[str]:
        return sorted(list(self._favorites))
