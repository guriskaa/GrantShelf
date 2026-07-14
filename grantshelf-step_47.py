# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: GrantShelf
# GrantShelf Demo: exercises the main workflow end-to-end.
from grant_shelf import GrantShelf, Opportunity

shelf = GrantShelf("2026-Q1")

opportunity = Opportunity(
    name="OpenAI Research Fellowship",
    deadline="2026-04-30",
    requirements=[
        "PhD or equivalent experience",
        "Published at a top AI venue",
        "$80k+ annual budget available",
        "Must have 2 years postdoc",
    ],
)

shelf.add(opportunity, tags=["AI", "fellowship"])

draft = shelf.draft("My proposal v1")
budget = shelf.budget(draft, {"personnel": "$60k", "travel": "$5k"})
review = shelf.review(draft, reviewer="Dr. A.", score=4)

print(shelf.report())
