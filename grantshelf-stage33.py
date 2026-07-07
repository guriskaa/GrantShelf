# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: GrantShelf
# GrantShelf – Settings module (Step 33)
import json
from pathlib import Path

GRANT_SHELF_SETTINGS_PATH = Path(__file__).parent / "settings.json"


def _default_settings() -> dict:
    return {
        "project_name": "GrantShelf",
        "currency": "$",
        "date_format": "%Y-%m-%d",
        "notification_email": "",
        "max_budget_pct_warning": 80,
        "review_score_threshold": 7.5,
    }


def _load_settings() -> dict:
    if GRANT_SHELF_SETTINGS_PATH.exists():
        return json.loads(GRANT_SHELF_SETTINGS_PATH.read_text())
    return _default_settings()


def get_settings() -> dict:
    """Return current settings (in-memory or file-backed)."""
    return _load_settings()


def update_setting(key: str, value) -> dict:
    """Update one setting and persist it. Returns the full updated dict."""
    settings = _load_settings()
    if key not in settings:
        raise KeyError(f"Unknown setting '{key}'. Known keys: {list(_default_settings())}")
    settings[key] = value
    GRANT_SHELF_SETTINGS_PATH.write_text(json.dumps(settings, indent=2))
    return settings


def reset_to_defaults() -> dict:
    """Reset all settings to defaults and persist. Returns the fresh dict."""
    new_settings = _default_settings()
    if GRANT_SHELF_SETTINGS_PATH.exists():
        GRANT_SHELF_SETTINGS_PATH.unlink()
    return new_settings
