# === Stage 51: Add unit tests for search and filter behavior ===
# Project: GrantShelf
import pytest
from grantshelf.models import GrantShelf, Opportunity


def test_search_by_keyword_filters_opportunities():
    shelf = GrantShelf()
    shelf.add(Opportunity("AI Research Fellowship", "Apply to the AI fellowship program"))
    shelf.add(Opportunity("Climate Science Grant", "Support climate research initiatives"))

    results = shelf.search("AI")
    assert len(results) == 1
    assert results[0].title == "AI Research Fellowship"


def test_filter_by_deadline_sorts_ascending():
    shelf = GrantShelf()
    shelf.add(Opportunity("Early Bird", "Description one"), deadline="2025-03-01")
    shelf.add(Opportunity("Late Bird", "Description two"), deadline="2026-01-15")

    filtered = shelf.filter_by_deadline(ascending=True)
    assert [o.title for o in filtered] == ["Early Bird", "Late Bird"]


def test_filter_by_min_budget_excludes_low():
    shelf = GrantShelf()
    shelf.add(Opportunity("Small Project", "Description one"), min_budget=5000, max_budget=10000)
    shelf.add(Opportunity("Big Project", "Description two"), min_budget=25000, max_budget=50000)

    filtered = shelf.filter_by_min_budget(20000)
    assert len(filtered) == 1
    assert filtered[0].title == "Big Project"


def test_search_empty_shelf_returns_none():
    shelf = GrantShelf()
    assert shelf.search("anything") is None
