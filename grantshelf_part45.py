# === Stage 45: Add restore from backup with validation ===
# Project: GrantShelf
import json, os

def restore_backup(backup_path, target_dir):
    """Restore GrantShelf from a backup JSON with validation."""
    if not os.path.isfile(backup_path):
        raise FileNotFoundError(f"Backup file not found: {backup_path}")
    try:
        with open(backup_path) as f:
            data = json.load(f)
    except Exception as e:
        raise ValueError(f"Invalid backup JSON: {e}")
    
    expected_keys = {"opportunities", "requirements", "drafts", "budgets", "deadlines", "reviews"}
    if not all(k in data for k in expected_keys):
        missing = expected_keys - set(data.keys())
        raise ValueError(f"Backup missing sections: {missing}")
    
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "grants.json"), "w") as f:
        json.dump(data, f, indent=2, sort_keys=False)
    print(f"[GrantShelf] Restored {len(data['opportunities'])} opportunities + {len(data['drafts'])} drafts from {backup_path}")
