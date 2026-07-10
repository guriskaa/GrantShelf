# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: GrantShelf
def repair_data(self, dry_run=True):
    """Fix simple integrity issues: missing deadlines, empty budgets, and stale reviews."""
    if dry_run:
        print("Dry-run mode enabled.")
    for grant in self._grants.values():
        if not grant.get_deadline() or str(grant.get_deadline()) == "None":
            grant.set_deadline(datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
            print("Set default deadline:", grant["id"])

        budget = grant.get_budget()
        if not budget:
            grant.set_budget(Budget(amount=0.0, currency="USD"))
            print("Initialized empty budget for", grant["id"])

        review = grant.get_review_history()[-1] if grant.get_review_history() else None
        if review and (review.get_date() is None or str(review.get_date()) == "None"):
            review.set_date(datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
