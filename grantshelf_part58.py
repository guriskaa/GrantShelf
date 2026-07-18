# === Stage 58: Add bulk update behavior for selected records ===
# Project: GrantShelf
def bulk_update_records(self, updates: dict[str, Any], ids: list[int]) -> list[GrantRecord]:
    """Update multiple records by ID with a single operation."""
    if not ids or not updates:
        return []
    for record in self._records.values():
        if record.id in ids:
            for key, value in updates.items():
                setattr(record, key, value)
            record.last_modified = datetime.datetime.now(datetime.timezone.utc)
            record.modified_by = self.current_user or "system"
    return [r for r in self._records.values() if r.id in ids]
