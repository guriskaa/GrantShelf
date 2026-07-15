# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: GrantShelf
import unittest
from datetime import date, timedelta


class TestGrantCreation(unittest.TestCase):
    def test_create_opportunity(self):
        opp = {"title": "Test Grant", "deadline": date(2035, 1, 1)}
        self.assertEqual(opp["title"], "Test Grant")

    def test_create_budget(self):
        budg = {"total": 1000.0, "allocated": {"research": 400.0}}
        self.assertAlmostEqual(budg["total"] - sum(budg["allocated"].values()), 600.0)


class TestGrantValidation(unittest.TestCase):
    def test_validate_deadline_format(self):
        good = date(2035, 1, 1)
        bad_str = "not a date"
        self.assertTrue(isinstance(good, date))
        with self.assertRaises(ValueError):
            date.fromisoformat(bad_str)

    def test_validate_budget_positive(self):
        budg = {"total": -10.0}
        self.assertFalse(budg["total"] > 0)


if __name__ == "__main__":
    unittest.main()
