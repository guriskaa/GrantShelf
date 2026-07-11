# === Stage 42: Add CSV export without external dependencies ===
# Project: GrantShelf
def export_to_csv(records):
    """Export grant records to a CSV string without external dependencies."""
    if not records:
        return ""
    headers = ["grant_id", "title", "deadline", "status"]
    lines = [",".join(headers)]
    for r in records:
        line = ",".join(str(r.get(h, "")) for h in headers)
        lines.append(line)
    return "\n".join(lines) + "\n"
