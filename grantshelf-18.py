# === Stage 18: Add an activity log with timestamps and action names ===
# Project: GrantShelf
import time
from datetime import datetime, timezone

class ActivityLog:
    def __init__(self):
        self._log = []

    def log(self, action_name: str, details: dict = None) -> None:
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "action": action_name,
            "details": details or {}
        }
        self._log.append(entry)

    def get_log(self) -> list:
        return sorted(self._log, key=lambda x: x["timestamp"], reverse=True)
