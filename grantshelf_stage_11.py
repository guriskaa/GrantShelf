# === Stage 11: Add JSON export for the current application state ===
# Project: GrantShelf
def export_state():
    import json, os
    base = "data"
    if not os.path.exists(base): return None
    state = {"opportunities": [], "requirements": [], "drafts": [], "budgets": [], "deadlines": [], "reviews": []}
    for f in ["opp.json", "req.json", "draft.json", "bud.json", "dl.json", "rev.json"]:
        path = os.path.join(base, f)
        if os.path.exists(path): state[f[:-5]] = json.load(open(path))
    return json.dumps(state, indent=2)
