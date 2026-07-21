# === Stage 66: Add export of a short status dashboard ===
# Project: GrantShelf
def export_status_dashboard(grants):
    dashboard = []
    for g in sorted(grants, key=lambda x: x.get_deadline()):
        status = "Open" if not g.is_closed() else "Closed"
        deadline = g.get_deadline().strftime("%Y-%m-%d") if hasattr(g.get_deadline(), 'strftime') else str(g.get_deadline())
        budget = f"${g.get_budget():,.0f}" if g.get_budget() is not None else "N/A"
        progress = g.get_progress() * 100
        review_count = len(g.get_reviews()) if hasattr(g, 'get_reviews') else 0
        dashboard.append({
            "name": g.get_name(),
            "status": status,
            "deadline": deadline,
            "budget": budget,
            "progress": progress,
            "reviews": review_count,
        })
    return {"dashboard": dashboard}
