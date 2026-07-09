# === Stage 38: Add data integrity checks for broken references ===
# Project: GrantShelf
def check_references(self):
    """Validate that all cross-references within GrantShelf are intact."""
    issues = []
    
    # Check opportunity references in requirements
    if self.requirements is not None:
        for req_id, req_data in self.requirements.items():
            if 'opportunity_id' in req_data and req_data['opportunity_id'] not in self.opportunities:
                issues.append(f"Requirement {req_id} references non-existent opportunity {req_data['opportunity_id']}")

    # Check requirement references in drafts
    if self.drafts is not None:
        for draft_id, draft_data in self.drafts.items():
            if 'requirement_ids' in draft_data:
                missing_reqs = [r for r in draft_data['requirement_ids'] if r not in self.requirements]
                if missing_reqs:
                    issues.append(f"Draft {draft_id} references non-existent requirements: {missing_reqs}")

    # Check budget references in budgets
    if self.budgets is not None:
        for budget_id, budget_data in self.budgets.items():
            if 'opportunity_id' in budget_data and budget_data['opportunity_id'] not in self.opportunities:
                issues.append(f"Budget {budget_id} references non-existent opportunity {budget_data['opportunity_id']}")

    # Check deadline references
    if self.deadlines is not None:
        for deadline_id, deadline_data in self.deadlines.items():
            if 'opportunity_id' in deadline_data and deadline_data['opportunity_id'] not in self.opportunities:
                issues.append(f"Deadline {deadline_id} references non-existent opportunity {deadline_data['opportunity_id']}")

    # Check review history references
    if self.review_history is not None:
        for review_id, review_data in self.review_history.items():
            if 'grant_id' in review_data and review_data['grant_id'] not in self.grants:
                issues.append(f"Review {review_id} references non-existent grant {review_data['grant_id']}")

    return issues
