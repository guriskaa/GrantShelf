# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: GrantShelf
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List

@dataclass
class Opportunity:
    id: str
    title: str
    agency: str
    deadline: date
    status: str = "open"
    notes: str = ""

@dataclass
class Requirement:
    opportunity_id: str
    description: str
    source_url: Optional[str] = None

@dataclass
class BudgetItem:
    category: str
    amount: float
    currency: str = "USD"

@dataclass
class GrantDraft:
    id: str
    title: str
    content: str
    budget_items: List[BudgetItem] = field(default_factory=list)
    status: str = "draft"
    created_at: date = field(default_factory=date.today)

@dataclass
class ReviewHistory:
    grant_id: str
    reviewer_name: str
    comments: str
    rating: Optional[int] = None
    reviewed_at: date = field(default_factory=date.today)
