# === Stage 53: Add command help text and usage examples ===
# Project: GrantShelf
def print_help():
    """Display GrantShelf command help and usage examples."""
    header = "GrantShelf — Command Reference\n"
    header += "=" * 40 + "\n\n"
    commands = [
        ("add-opportunity", "Add a new grant opportunity with title, deadline, amount, url, and tags."),
        ("add-requirement", "Create a requirement entry: description, priority (critical/high/medium/low), status."),
        ("add-draft", "Begin a draft application: set working dir, add sections, attach files, save as .gds."),
        ("add-budget", "Record budget line items: category, amount, currency, notes. Supports CSV import."),
        ("add-deadline", "Log an internal or external deadline with date, description, and completion status."),
        ("add-review", "Save a review entry containing reviewer name, score (1-5), comments, and timestamp."),
        ("list-opportunities", "Show all tracked opportunities in table format with sort/filter options."),
        ("list-drafts", "Display active drafts grouped by project/section with progress bars."),
        ("list-deadlines", "List upcoming deadlines sorted by date; highlight overdue items in red."),
        ("list-reviews", "Summarize review history per draft: average score and recent feedback."),
        ("export", "Export entire shelf data to JSON, CSV, or Markdown formats for backup/sharing."),
    ]
    print(header)
    for cmd, desc in commands:
        print(f"  {cmd:<25} — {desc}")
    print("\nUsage examples:\n")
    print("  gds add-opportunity --title 'AI Research' --deadline 2024-12-31 --amount 50000 --url https://example.org/grants\n")
    print("  gds list-deadlines --format table --sort date\n")
    print("  gds export --format json --output grants.json\n")
