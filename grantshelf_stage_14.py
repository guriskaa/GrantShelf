# === Stage 14: Add file load support with fallback demo data ===
# Project: GrantShelf
import json, os
from pathlib import Path

def load_data(path: str = "data.json"):
    try:
        with open(path) as f: return json.load(f)
    except FileNotFoundError:
        demo = {
            "opportunities": [{"id": 1, "title": "AI Research", "deadline": "2024-12-31"}],
            "requirements": [{"opportunity_id": 1, "doc_type": "Proposal", "max_pages": 15}],
            "drafts": [], "budgets": [], "deadlines": [], "reviews": []
        }
        Path(path).write_text(json.dumps(demo, indent=2))
        return demo
