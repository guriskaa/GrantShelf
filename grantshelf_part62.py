# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: GrantShelf
def score_opportunity(opportunity: dict) -> float:
    """Return a simple priority score for an opportunity."""
    score = 0.0
    if opportunity.get("deadline", ""):
        import datetime
        days_left = (datetime.date.today() + datetime.timedelta(days=30)).isoformat() - opportunity["deadline"].isoformat()
        if days_left > 0:
            score += min(10, max(0, days_left / 7))
    for req in opportunity.get("requirements", []):
        if req in opportunity.get("drafts", {}):
            score += 5
        elif req in ["Funding Source", "Topic"]:
            score += 2
    return round(score, 1)
