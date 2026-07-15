# === Stage 50: Add unit tests for import and export behavior ===
# Project: GrantShelf
import unittest
from datetime import date, timedelta
from grantshelf.models.opportunity import Opportunity
from grantshelf.models.requirement import Requirement
from grantshelf.models.draft import Draft
from grantshelf.models.budget import Budget
from grantshelf.models.deadline import Deadline
from grantshelf.models.review import Review

class TestImportExport(unittest.TestCase):
    def test_export_and_import_opportunity(self):
        opp = Opportunity(id="opp1", title="Test Grant", deadline=date(2024, 6, 30))
        data = opp.to_dict()
        self.assertIn("id", data)
        self.assertEqual(data["title"], "Test Grant")

    def test_export_and_import_requirement(self):
        req = Requirement(id="req1", title="Budget Required", amount=5000)
        data = req.to_dict()
        self.assertIn("amount", data)
        self.assertEqual(data["amount"], 5000)

    def test_export_and_import_draft(self):
        draft = Draft(id="draft1", body="Initial proposal")
        data = draft.to_dict()
        self.assertIn("body", data)
        self.assertEqual(data["body"], "Initial proposal")

    def test_export_and_import_budget(self):
        budget = Budget(id="budget1", total=10000, spent=3000)
        data = budget.to_dict()
        self.assertIn("spent", data)
        self.assertEqual(data["spent"], 3000)

    def test_export_and_import_deadline(self):
        dl = Deadline(id="dl1", date=date(2024, 7, 15), status="pending")
        data = dl.to_dict()
        self.assertIn("status", data)
        self.assertEqual(data["status"], "pending")

    def test_export_and_import_review(self):
        rev = Review(id="rev1", author="Alice", date=date(2024, 5, 1), score=8.5)
        data = rev.to_dict()
        self.assertIn("score", data)
        self.assertEqual(data["score"], 8.5)

    def test_roundtrip_opportunity(self):
        opp = Opportunity(id="opp1", title="Round Trip Grant", deadline=date(2024, 9, 30))
        loaded = Opportunity.from_dict(opp.to_dict())
        self.assertEqual(loaded.title, "Round Trip Grant")
        self.assertEqual(loaded.deadline, date(2024, 9, 30))

    def test_roundtrip_requirement(self):
        req = Requirement(id="req1", title="Must Have Budget", amount=7500)
        loaded = Requirement.from_dict(req.to_dict())
        self.assertEqual(loaded.amount, 7500)

if __name__ == "__main__":
    unittest.main()
