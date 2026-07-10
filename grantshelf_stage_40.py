# === Stage 40: Add plain text report export ===
# Project: GrantShelf
def export_report(shelf, path="report.txt"):
    with open(path, "w") as f:
        f.write(f"GrantShelf Report - {shelf.now.strftime('%Y-%m-%d')}\n")
        for opp in shelf.opportunities:
            status = opp.status.value if hasattr(opp, 'status') else '?'
            f.write(f"- [{opp.id}] {opp.title} | Status: {status}")
            if opp.deadline and opp.deadline <= shelf.now:
                f.write(" [EXPIRED]")
            f.write("\n")
        for draft in shelf.drafts:
            f.write(f"- Draft: {draft.name} ({len(draft.pages)} pages)\n")
        for review in shelf.reviews:
            f.write(f"- Review: {review.target} -> {review.assessment}\n")
