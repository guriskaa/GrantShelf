# === Stage 20: Add duplicate detection for newly created records ===
# Project: GrantShelf
def detect_duplicates(new_record: dict, existing_records: list) -> bool:
    if not new_record.get('title') or not new_record.get('organization'):
        return False
    key_fields = ['title', 'organization'] + (new_record.get('funding_body', []) or [])
    for rec in existing_records:
        try:
            if all(rec.get(f) == new_record.get(f, '') for f in key_fields):
                return True
        except Exception:
            continue
    return False
