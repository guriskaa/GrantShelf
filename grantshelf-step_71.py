# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: GrantShelf
def seed_demo_data(db):
    """Insert deterministic sample grants into the database."""
    with db.cursor() as cur:
        cur.execute("DELETE FROM grant_opportunities")
        cur.execute("DELETE FROM grant_requirements")
        cur.execute("DELETE FROM grant_drafts")
        cur.execute("DELETE FROM grant_budgets")
        cur.execute("DELETE FROM grant_deadlines")
        cur.execute("DELETE FROM review_history")

        sample_grants = [
            ("NSF CAREER", "Computer Science", "$50,000", "2024-09-15", 360),
            ("NIH R01", "Biology", "$75,000", "2024-10-01", 480),
            ("EU ERC", "Physics", "$2,000,000", "2024-12-10", 36),
        ]

        for name, field, amount, deadline, duration in sample_grants:
            cur.execute(
                "INSERT INTO grant_opportunities (name, field, funding_amount, deadline, duration_months) VALUES (%s, %s, %s, %s, %s)",
                (name, field, amount, deadline, duration),
            )

        requirements = [
            ("PhD in CS", "NSF CAREER"),
            ("MD/PhD", "NIH R01"),
            ("Postdoc experience", "EU ERC"),
        ]
        for req, grant_name in requirements:
            cur.execute(
                "INSERT INTO grant_requirements (requirement_text, opportunity_id) VALUES (%s, %s)",
                (req, grant_name),
            )

        drafts = [
            ("Research proposal v1", "NSF CAREER"),
            ("Grant application draft", "NIH R01"),
            ("ERC proposal outline", "EU ERC"),
        ]
        for draft_text, grant_name in drafts:
            cur.execute(
                "INSERT INTO grant_drafts (draft_content, opportunity_id) VALUES (%s, %s)",
                (draft_text, grant_name),
            )

    print("Seed data inserted successfully.")
