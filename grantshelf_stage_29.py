# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: GrantShelf
from datetime import datetime, timedelta
def get_upcoming_deadlines(deadlines: list[dict], days_ahead: int = 7) -> list[tuple[str, str]]:
    today = datetime.now().date()
    cutoff = today + timedelta(days=days_ahead)
    results = []
    for item in deadlines:
        due_date_str = item.get("due_date", "")
        if not due_date_str:
            continue
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
            if today <= due_date <= cutoff:
                results.append((item["grant_id"], f"Due {due_date}: {item['title']}"))
        except ValueError:
            continue
    return sorted(results, key=lambda x: datetime.strptime(x[1].split(":")[0], "%Y-%m-%d").date())

def get_upcoming_reviews(reviews: list[dict], days_ahead: int = 7) -> list[tuple[str, str]]:
    today = datetime.now().date()
    cutoff = today + timedelta(days=days_ahead)
    results = []
    for item in reviews:
        review_date_str = item.get("review_date", "")
        if not review_date_str:
            continue
        try:
            review_date = datetime.strptime(review_date_str, "%Y-%m-%d").date()
            if today <= review_date <= cutoff:
                results.append((item["grant_id"], f"Review due {review_date}: {item['title']}"))
        except ValueError:
            continue
    return sorted(results, key=lambda x: datetime.strptime(x[1].split(":")[0], "%Y-%m-%d").date())

def get_upcoming_budgets(budgets: list[dict], days_ahead: int = 7) -> list[tuple[str, str]]:
    today = datetime.now().date()
    cutoff = today + timedelta(days=days_ahead)
    results = []
    for item in budgets:
        budget_date_str = item.get("budget_deadline", "")
        if not budget_date_str:
            continue
        try:
            budget_date = datetime.strptime(budget_date_str, "%Y-%m-%d").date()
            if today <= budget_date <= cutoff:
                results.append((item["grant_id"], f"Budget due {budget_date}: {item['title']}"))
        except ValueError:
            continue
    return sorted(results, key=lambda x: datetime.strptime(x[1].split(":")[0], "%Y-%m-%d").date())
