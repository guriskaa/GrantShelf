# === Stage 43: Add CSV import for the primary record type ===
# Project: GrantShelf
def import_opportunities(csv_path, delimiter=","):
    records = []
    with open(csv_path, "r", newline="") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        for row in reader:
            record = {
                "title": row.get("title", "").strip(),
                "description": row.get("description", "").strip(),
                "deadline": row.get("deadline", "").strip(),
                "budget": row.get("budget", "").strip().replace("$", "").replace(",", ""),
                "requirements": row.get("requirements", "").strip(),
                "status": row.get("status", "open").strip(),
            }
            if record["title"]:
                records.append(record)
    return records
