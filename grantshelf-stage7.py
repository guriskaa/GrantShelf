# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: GrantShelf
def format_deadline(deadline: str, today: datetime.date) -> str:
    if deadline is None: return "No date"
    try: d = datetime.datetime.strptime(deadline, "%Y-%m-%d").date()
    except ValueError: return f"[Invalid: {deadline}]"
    delta = (today - d).days
    if delta < 0: return f"<{abs(delta)} days overdue>"
    elif delta <= 7: return f"⚠️ Due in {delta} day(s)"
    elif delta <= 30: return f"In {delta} days"
    else: return "Scheduled"

def format_budget(budget: dict) -> str:
    if not budget: return "(No budget defined)"
    lines = [f"Total Requested: ${budget.get('total', 0):,.2f}"]
    for cat, amount in sorted(budget.items()):
        lines.append(f"  • {cat}: ${amount:,.2f}")
    return "\n".join(lines)

def format_review(review: dict) -> str:
    if not review: return "(No reviews yet)"
    reviewer = review.get("reviewer", "Anonymous")
    score = review.get("score", "?")
    comment = review.get("comment", "")[:60] + ("..." if len(comment)>60 else "")
    date = review.get("date", "") or ""
    return f"{reviewer}: {score}/10 — {comment} ({date})"

def format_opportunity(op: dict) -> str:
    title = op.get("title", "Untitled")[:45] + ("..." if len(title)>45 else "")
    deadline_str = format_deadline(op.get("deadline"), datetime.date.today())
    budget_str = format_budget(op.get("budget"))
    review_str = format_review(op.get("review_history")[0]) if op.get("review_history") else "(No reviews)"
    return f"[{title}]\n  Deadline: {deadline_str}\n  Budget:\n{budget_str}\n  Review:\n{review_str}"
