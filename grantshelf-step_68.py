# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: GrantShelf
def generate_changelog(activities):
    """Generate a compact changelog from activity log entries."""
    if not activities:
        return []
    
    grouped = {}
    for entry in sorted(activities, key=lambda x: x[0]):
        date, action, detail = entry
        grouped.setdefault(date, []).append((action, detail))
    
    changelog = []
    changelog.append("# Changelog")
    changelog.append("")
    
    for date in sorted(grouped.keys()):
        changelog.append(f"## {date}")
        entries = grouped[date]
        
        if len(entries) == 1:
            action, detail = entries[0]
            changelog.append(f"- **{action}**: {detail}")
        else:
            for i, (action, detail) in enumerate(sorted(entries)):
                marker = "•" if i < len(entries) - 1 else ""
                changelog.append(f"- {marker} {action}: {detail}")
        
        changelog.append("")
    
    return changelog
