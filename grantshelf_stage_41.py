# === Stage 41: Add plain text import for a simple line-based format ===
# Project: GrantShelf
def parse_line_record(text: str):
    """Parse a simple line-based record format."""
    parts = text.strip().split("|")
    if len(parts) < 4:
        raise ValueError(f"Invalid record length: {len(parts)}")
    return {
        "id": int(parts[0]),
        "title": parts[1].strip(),
        "status": parts[2].strip(),
        "deadline": parts[3].strip() if len(parts) > 3 else "",
    }

def format_line_record(record: dict) -> str:
    """Serialize a record back to line-based format."""
    return f"{record['id']}|{record['title']}|{record['status']}|{record.get('deadline', '')}"
