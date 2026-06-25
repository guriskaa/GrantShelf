# === Stage 4: Implement create operations for the primary records ===
# Project: GrantShelf
from datetime import date, timedelta
import uuid

class GrantRecord:
    def __init__(self, title, deadline, status="open", requirements=None):
        self.id = str(uuid.uuid4())[:8]
        self.title = title
        self.deadline = date.fromisoformat(deadline) if isinstance(deadline, str) else deadline
        self.status = status
        self.requirements = requirements or []

    def is_expired(self):
        return date.today() > self.deadline

class OpportunityManager:
    _instances = {}

    @classmethod
    def get(cls):
        if cls._instances.get("default"):
            return cls._instances["default"]
        instance = cls()
        cls._instances["default"] = instance
        return instance

    def add_opportunity(self, title, deadline, requirements=None):
        record = GrantRecord(title=title, deadline=deadline, status="open", requirements=requirements)
        self.opportunities.append(record)
        print(f"Added opportunity: {record.title} (ID: {record.id})")

    def add_draft(self, content, title="Untitled Draft"):
        draft_id = str(uuid.uuid4())[:8]
        self.drafts[title] = {"content": content, "id": draft_id, "created_at": date.today()}
        print(f"Created draft: {draft_id}")

    def add_budget(self, category, amount):
        budget_entry = {"category": category, "amount": float(amount), "date": date.today()}
        self.budgets.append(budget_entry)
        print(f"Added budget entry for {category}: {amount}")

    def set_deadline_reminder(self, grant_id, days_before=7):
        today = date.today()
        target_date = today + timedelta(days=days_before)
        reminders.append({"grant_id": grant_id, "date": target_date.isoformat(), "status": "pending"})
