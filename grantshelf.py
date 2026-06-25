# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: GrantShelf
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional
import uuid

@dataclass
class Grant:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    deadline: date | None = None
    status: str = "open"  # open, closed, awarded
    requirements: List[str] = field(default_factory=list)

@dataclass
class Budget:
    category: str
    amount: float
    notes: str = ""

@dataclass
class GrantShelfApp:
    opportunities: dict[str, Grant] = field(default_factory=dict)
    drafts: dict[str, List[Budget]] = field(default_factory=dict)
    review_history: List[dict] = field(default_factory=list)

def init_demo():
    app = GrantShelfApp()
    
    # Demo Opportunity 1
    opp1 = Grant(title="Green Energy Research", deadline=date(2025, 3, 15), status="open")
    opp1.requirements = ["Python expertise", "Data analysis experience"]
    app.opportunities["opp-001"] = opp1
    
    # Demo Opportunity 2
    opp2 = Grant(title="AI for Education", deadline=date(2024, 12, 31), status="open")
    opp2.requirements = ["ML background", "Educational domain knowledge"]
    app.opportunities["opp-002"] = opp2
    
    # Demo Draft Budget
    draft_id = str(uuid.uuid4())[:8]
    app.drafts[draft_id] = [
        Budget(category="Personnel", amount=15000.0, notes="Senior researcher"),
        Budget(category="Equipment", amount=5000.0, notes="Servers and GPUs")
    ]
    
    # Demo Review Entry
    app.review_history.append({
        "date": date.today(),
        "grant_id": "opp-001",
        "reviewer_notes": "Strong technical proposal, budget looks realistic."
    })
    
    return app

if __name__ == "__main__":
    shelf = init_demo()
    print(f"Loaded {len(shelf.opportunities)} opportunities")
