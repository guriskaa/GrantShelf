# === Stage 26: Add weekly summary calculations ===
# Project: GrantShelf
def calculate_weekly_summary(grants):
    from datetime import date, timedelta
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(weeks=1)
    summary = {"opportunities": 0, "deadlines_passed": 0, "active_deadlines": 0}
    for grant in grants:
        if grant.get("status") == "open" and week_start <= date.fromisoformat(grant["deadline"]) < today:
            summary["opportunities"] += 1
        deadline = date.fromisoformat(grant["deadline"])
        if deadline < today:
            summary["deadlines_passed"] += 1
        elif deadline >= week_start and deadline <= week_end:
            summary["active_deadlines"] += 1
    return summary
