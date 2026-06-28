# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: GrantShelf
class GrantSorter:
    def __init__(self, grants):
        self.grants = grants

    def sort_by_title(self) -> list[dict]:
        return sorted(self.grants, key=lambda g: (g.get('title', '').lower(), g.get('id', '')))

    def sort_by_deadline(self) -> list[dict]:
        return sorted(self.grants, key=lambda g: g.get('deadline') or datetime.max)

    def sort_by_priority(self) -> list[dict]:
        priority_map = {'High': 0, 'Medium': 1, 'Low': 2}
        return sorted(self.grants, key=lambda g: priority_map.get(g.get('priority', 'Medium'), 1))

    def sort_by_updated_at(self) -> list[dict]:
        return sorted(self.grants, key=lambda g: g.get('updated_at') or datetime.min)
