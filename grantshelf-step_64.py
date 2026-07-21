# === Stage 64: Add validation for relationship references ===
# Project: GrantShelf
from datetime import date, timedelta

def validate_grant_timeline(grant):
    """Enforce temporal consistency: deadlines must be after requirements and budget dates."""
    if grant.requirements_deadline and grant.deadline:
        gap = (grant.deadline - grant.requirements_deadline).days
        assert gap >= 0, "Deadline cannot precede the requirements deadline."

    if grant.budget_start_date and grant.budget_end_date:
        budget_gap = (grant.budget_end_date - grant.budget_start_date).days
        assert budget_gap > 0 or budget_gap == 0, \
            "Budget period must be non-negative."

    return grant
