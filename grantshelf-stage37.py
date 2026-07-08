# === Stage 37: Add recommendations for the next useful action ===
# Project: GrantShelf
def suggest_next_action(self):
    """Return a human-readable suggestion based on current state."""
    if not self.grants:
        return "Add your first grant opportunity."
    pending = [g for g in self.grants if not g.get("status")]
    if pending:
        return f"Continue working on one of the {len(pending)} pending grants."
    drafts = [g for g in self.grants if g.get("phase") == "draft"]
    if drafts:
        return f"Finalize your {len(drafts)} grant draft(s)."
    reviews = [g for g in self.grants if g.get("reviewed")]
    if reviews:
        return "Review the outcomes of your previously submitted grants."
    return "All grants are complete. Consider starting a new opportunity."
