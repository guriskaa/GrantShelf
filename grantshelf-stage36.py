# === Stage 36: Add templates for quickly creating common records ===
# Project: GrantShelf
# GrantShelf: Quick templates for common record types
from datetime import date, timedelta
from .models import Opportunity, Requirement, Draft, Budget, Deadline, Review


def template_opportunity(name: str = "New Grant") -> Opportunity:
    return Opportunity(
        title=name,
        organization="",
        deadline=date.today() + timedelta(days=30),
        notes="",
    )


def template_requirement(opportunity_id: int) -> Requirement:
    return Requirement(
        opportunity_id=opportunity_id,
        name=f"Requirement for {opportunity_id}",
        description="Describe the requirement here.",
        deadline=date.today() + timedelta(days=14),
    )


def template_draft(requirement_ids: list[int]) -> Draft:
    return Draft(
        requirements=requirement_ids,
        title="Draft Proposal",
        body="# Draft content\n",
        status="IN_PROGRESS",
    )


def template_budget(draft_id: int) -> Budget:
    return Budget(
        draft_id=draft_id,
        total_amount=0.0,
        currency="USD",
        line_items=[{"category": "Personnel", "amount": 0.0}],
    )


def template_deadline(task_name: str = "Review") -> Deadline:
    return Deadline(
        task_name=task_name,
        due_date=date.today() + timedelta(days=7),
        priority="MEDIUM",
        notes="",
    )


def template_review(draft_id: int) -> Review:
    return Review(
        draft_id=draft_id,
        reviewer="internal",
        score=None,
        comments="",
        created=date.today(),
    )
