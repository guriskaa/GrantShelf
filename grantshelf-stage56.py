# === Stage 56: Add compact error classes for domain failures ===
# Project: GrantShelf
class GrantShelfError(Exception):
    pass


class OpportunityNotFoundError(GrantShelfError):
    def __init__(self, opportunity_id: str) -> None:
        self.opportunity_id = opportunity_id
        super().__init__(f"Opportunity '{opportunity_id}' not found")


class RequirementConflictError(GrantShelfError):
    def __init__(self, field: str, expected: object, got: object) -> None:
        self.field = field
        self.expected = expected
        self.got = got
        super().__init__(f"Requirement conflict on '{field}': expected {expected}, got {got}")


class BudgetExceededError(GrantShelfError):
    def __init__(self, category: str, planned: float, available: float) -> None:
        self.category = category
        self.planned = planned
        self.available = available
        super().__init__(f"Budget exceeded for '{category}': planned ${planned}, available ${available}")


class DeadlineOverrunError(GrantShelfError):
    def __init__(self, deadline: str, days_over: int) -> None:
        self.deadline = deadline
        self.days_over = days_over
        super().__init__(f"Deadline '{deadline}' overrun by {days_over} days")


class ReviewHistoryInconsistentError(GrantShelfError):
    def __init__(self, reviewer: str, grant_id: str) -> None:
        self.reviewer = reviewer
        self.grant_id = grant_id
        super().__init__(f"Review history inconsistent for reviewer '{reviewer}' on grant '{grant_id}'")


class GrantShelfIntegrityError(GrantShelfError):
    def __init__(self, message: str) -> None:
        super().__init__(message)
