# === Stage 27: Add monthly summary calculations ===
# Project: GrantShelf
def calculate_monthly_summary(grants):
    from collections import defaultdict
    monthly = defaultdict(lambda: {"total": 0, "count": 0})
    for g in grants:
        if hasattr(g, 'deadline') and g.deadline:
            try:
                month_key = g.deadline.strftime("%Y-%m")
            except AttributeError:
                continue
            monthly[month_key]["total"] += g.budget
            monthly[month_key]["count"] += 1
    summary = []
    for m in sorted(monthly.keys()):
        data = monthly[m]
        avg = data["total"] / data["count"] if data["count"] > 0 else 0.0
        summary.append({
            "month": m,
            "opportunities": data["count"],
            "budget_total": data["total"],
            "avg_budget": round(avg, 2)
        })
    return summary
