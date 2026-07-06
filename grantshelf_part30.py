# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: GrantShelf
import datetime


def _parse_date(raw, fmt=None):
    if raw is None:
        return None
    if isinstance(raw, datetime.datetime):
        return raw.date()
    if isinstance(raw, str):
        for f in (fmt or "%Y-%m-%d", "%Y/%m/%d", "%m/%d/%Y"):
            try:
                return datetime.datetime.strptime(raw.strip(), f).date()
            except ValueError:
                continue
        raise ValueError(
            f"Cannot parse date string '{raw!r}'. "
            "Accepted formats: YYYY-MM-DD, YYYY/MM/DD, MM/DD/YYYY."
        )
    if isinstance(raw, (int, float)):
        return datetime.datetime.fromtimestamp(float(raw)).date()
    raise TypeError(f"Expected str/int/float/datetime, got {type(raw).__name__}.")


def parse_date(value):
    """Parse a date from string, int/float timestamp, or datetime object.

    Returns a date object (or None if input is None). Raises ValueError with a
    clear message on failure."""
    return _parse_date(value)
