# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: GrantShelf
def update_grant_record(grants_db, grant_id, updates):
    if grants_db.get(grant_id) is None:
        raise ValueError(f"Grant {grant_id} not found")
    
    record = dict(grants_db[grant_id])
    for key, value in updates.items():
        if key == "status":
            allowed_statuses = ["draft", "reviewing", "submitted", "awarded", "rejected"]
            if value not in allowed_statuses:
                raise ValueError(f"Invalid status '{value}'. Must be one of {allowed_statuses}")
        elif key == "budget":
            try:
                record[key] = float(value)
            except (TypeError, ValueError):
                raise ValueError("Budget must be a number")
        else:
            record[key] = value
    
    grants_db[grant_id] = record
    return grant_id
