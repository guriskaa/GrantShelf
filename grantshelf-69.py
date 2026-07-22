# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: GrantShelf
def reset_demo_data(db):
    """Reset demo data for manual testing."""
    db.drop_table("review_history")
    db.drop_table("deadlines")
    db.drop_table("budgets")
    db.drop_table("drafts")
    db.drop_table("requirements")
    db.drop_table("opportunities")
    db.create_all()

reset_demo_data(db)
