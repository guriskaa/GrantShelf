# === Stage 72: Add Markdown report export ===
# Project: GrantShelf
def export_markdown_report(self, path=None):
    if path is None:
        path = f"grantshelf_{self.project_name}.md"
    with open(path, "w") as f:
        f.write(f"# GrantShelf Report: {self.project_name}\n\n")
        for op in self.opportunities.values():
            f.write(f"## Opportunity: {op.get('name', 'Untitled')}\n")
            deadline = op.get("deadline", "N/A")
            requirements = op.get("requirements", [])
            drafts = op.get("drafts", [])
            budget = op.get("budget", 0)
            f.write(f"- **Deadline:** {deadline}\n")
            f.write(f"- **Requirements:** {'; '.join(requirements)}\n")
            f.write(f"- **Budget:** ${budget:,.2f}\n")
            f.write(f"- **Drafts:** {len(drafts)}\n\n")
        self._write_review_history(f)
    print(f"Markdown report exported to {path}")
