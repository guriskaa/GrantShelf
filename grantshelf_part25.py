# === Stage 25: Add daily summary calculations ===
# Project: GrantShelf
def calculate_daily_summary(grants):
    """Compute daily summary metrics for all grants."""
    if not grants:
        return {"total_opportunities": 0, "active_deadlines_today": 0}
    
    today = datetime.date.today()
    total_budget = sum(g.get("budget", {}).get("amount", 0) for g in grants.values())
    active_deadlines = [g for g in grants.values() if g.get("deadline") and g["deadline"].date() == today]
    
    return {
        "total_opportunities": len(grants),
        "active_deadlines_today": len(active_deadlines),
        "total_budget": total_budget,
        "urgent_count": sum(1 for g in grants.values() if g.get("deadline") and (g["deadline"] - today).days <= 3)
    }
