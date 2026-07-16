# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: GrantShelf
def _format_deadline(deadline_str, reference_date=None):
    """Return a human-readable deadline string, optionally compared to a date."""
    if reference_date is None:
        from datetime import datetime
        today = datetime.now().date()
    else:
        today = reference_date.date()

    try:
        dt = datetime.strptime(deadline_str, "%Y-%m-%d").date()
    except ValueError:
        return deadline_str

    delta = (dt - today).days
    if delta < 0:
        return f"⚠ Overdue by {abs(delta)} days"
    elif delta == 0:
        return "🔴 Today's deadline!"
    elif delta <= 30:
        return f"⏳ Due in {delta} days"
    else:
        return deadline_str
