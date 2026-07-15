# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: GrantShelf
def test_update_missing_id(self):
    shelf = GrantShelf()
    assert shelf._grant_by_id("nonexistent") is None


def test_delete_nonexistent(self):
    shelf = GrantShelf()
    shelf.delete_grant("nope")  # should be a no-op, dict remains empty
    assert len(shelf.grants) == 0


def test_update_preserves_other_fields(self):
    grant = {"id": "g1", "title": "Old", "deadline": "2099-01-01"}
    shelf = GrantShelf()
    shelf.add_grant(grant)
    shelf.update_grant("g1", {"title": "New"})
    updated = list(shelf.grants.values())[0]
    assert updated["title"] == "New"
    assert updated["deadline"] == "2099-01-01"
