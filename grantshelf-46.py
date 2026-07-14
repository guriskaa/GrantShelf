# === Stage 46: Add a schema version field and migration helper ===
# Project: GrantShelf
def migrate_to_v1():
    """Schema v1: adds schema_version column."""
    with open("schema", "r") as f:
        lines = f.readlines()
    if any(line.strip().startswith("CREATE TABLE grants (") for line in lines):
        return  # already migrated
    new_lines = []
    for i, line in enumerate(lines):
        if "CREATE TABLE grants (" in line and ")" not in line:
            new_lines.append(line)
            new_lines.append('    schema_version INTEGER NOT NULL DEFAULT 1,\n')
            break
        elif ")" in line and i > 0 and any("schema_version" in l for l in lines[:i+1]):
            new_lines.append(line)
            break
        else:
            new_lines.append(line)
    with open("schema", "w") as f:
        f.writelines(new_lines)
