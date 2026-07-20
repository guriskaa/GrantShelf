# === Stage 63: Add relationships between records where useful ===
# Project: GrantShelf
class GrantShelf:
    def __init__(self):
        self.opportunities = {}
        self.requirements = {}
        self.drafts = {}
        self.budgets = {}
        self.deadlines = {}
        self.review_history = []

    def add_relationship(self, opp_id, req_ids=None, draft_ids=None, budget_ids=None, deadline_ids=None):
        if not opp_id:
            return "opportunity id required"
        if not isinstance(opp_id, str) or len(opp_id) != 32:
            return "invalid opportunity id format (must be a 32-char string)"
        self.opportunities[opp_id] = {
            'id': opp_id,
            'requirements': req_ids or [],
            'drafts': draft_ids or [],
            'budgets': budget_ids or [],
            'deadlines': deadline_ids or []
        }
        return "relationship added"

    def get_relationship(self, opp_id):
        if not isinstance(opp_id, str) or len(opp_id) != 32:
            return None
        rel = self.opportunities.get(opp_id, {})
        if not rel:
            return None
        return {
            'requirements': rel.get('requirements', []),
            'drafts': rel.get('drafts', []),
            'budgets': rel.get('budgets', []),
            'deadlines': rel.get('deadlines', [])
        }

    def get_summary(self):
        return {
            'opportunities_count': len(self.opportunities),
            'total_relationships': sum(len(v['requirements']) + len(v['drafts']) + len(v['budgets']) + len(v['deadlines']) for v in self.opportunities.values())
        }

    def get_all_records(self):
        all_data = []
        all_data.extend({'type': 'opportunity', **opp} for opp in self.opportunities.values())
        all_data.extend({'type': 'requirement', **req} for req in self.requirements.values())
        all_data.extend({'type': 'draft', **dra} for dra in self.drafts.values())
        all_data.extend({'type': 'budget', **bud} for bud in self.budgets.values())
        all_data.extend({'type': 'deadline', **dea} for dea in self.deadlines.values())
        return all_data
