# === Stage 28: Add overdue item detection based on due dates ===
# Project: GrantShelf
from datetime import date, timedelta

def check_overdue_items(items):
    today = date.today()
    overdue = []
    for item in items:
        if hasattr(item, 'deadline') and item.deadline < today:
            days_left = (item.deadline - today).days
            status = "OVERDUE" if days_left < 0 else "PENDING"
            overdue.append({**item, 'status': status, 'days_overdue': abs(days_left)})
    return overdue
