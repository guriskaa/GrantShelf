# === Stage 60: Add saved views for frequently used filters ===
# Project: GrantShelf
class SavedView:
    def __init__(self, name, filters=None, sort_by="deadline", order="asc"):
        self.name = name
        self.filters = filters or {}
        self.sort_by = sort_by
        self.order = order

    @staticmethod
    def apply(view, shelf):
        for key, val in view.filters.items():
            if hasattr(shelf, "filter_") and callable(getattr(shelf, "filter_", None)):
                getattr(shelf, "filter_")(key, val)
        return shelf.sort(sort_by=view.sort_by, order=view.order)

    def __repr__(self):
        return f"<SavedView '{self.name}': {self.filters}, sort={self.sort_by}/{self.order}>"
