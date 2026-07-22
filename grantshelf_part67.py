# === Stage 67: Add a function that returns key project metrics ===
# Project: GrantShelf
def project_metrics(opportunities, requirements, drafts, budgets, deadlines, reviews):
    """Return a compact dict of key GrantShelf metrics."""
    return {
        "total_opportunities": len(opportunities),
        "filled_requirements": sum(1 for r in requirements if r["status"] == "completed"),
        "draft_count": len(drafts),
        "approved_budgets": sum(1 for b in budgets if b["approved"]),
        "upcoming_deadlines": [d for d in deadlines if d["date"] > datetime.now().date()][:5],
        "recent_reviews": reviews[-3:] if len(reviews) >= 3 else reviews,
    }
