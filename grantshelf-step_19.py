# === Stage 19: Add undo support for the last simple mutation ===
# Project: GrantShelf
import json
from typing import Optional, List, Dict, Any
from datetime import datetime

class GrantShelf:
    def __init__(self):
        self.history_stack: List[Dict[str, Any]] = []
    
    def _snapshot(self) -> None:
        state = {
            'history': list(self.history_stack),
            'timestamp': datetime.now().isoformat()
        }
        self.history_stack.append(state)

    def add_opportunity(self, title: str, deadline: str, requirements: List[str]) -> bool:
        if not self._can_undo(): return False
        self._snapshot()
        entry = {'type': 'opportunity', 'title': title, 'deadline': deadline, 'requirements': requirements}
        self.opportunities.append(entry)
        return True

    def add_draft(self, opportunity_id: str, content: str) -> bool:
        if not self._can_undo(): return False
        self._snapshot()
        entry = {'type': 'draft', 'opportunity_id': opportunity_id, 'content': content}
        self.drafts.append(entry)
        return True

    def add_budget(self, opportunity_id: str, amount: float, breakdown: Dict[str, float]) -> bool:
        if not self._can_undo(): return False
        self._snapshot()
        entry = {'type': 'budget', 'opportunity_id': opportunity_id, 'amount': amount, 'breakdown': breakdown}
        self.budgets.append(entry)
        return True

    def add_deadline(self, opportunity_id: str, new_date: str) -> bool:
        if not self._can_undo(): return False
        self._snapshot()
        entry = {'type': 'deadline', 'opportunity_id': opportunity_id, 'new_date': new_date}
        self.deadlines.append(entry)
        return True

    def add_review(self, opportunity_id: str, score: float, comments: str) -> bool:
        if not self._can_undo(): return False
        self._snapshot()
        entry = {'type': 'review', 'opportunity_id': opportunity_id, 'score': score, 'comments': comments}
        self.reviews.append(entry)
        return True

    def _can_undo(self) -> bool:
        return len(self.history_stack) < 10 and not self._is_locked()

    def undo_last(self) -> Optional[Dict[str, Any]]:
        if not self.history_stack: return None
        last_state = self.history_stack.pop()
        restored_data = {k: v for k, v in last_state.items() if k != 'timestamp'}
        self.opportunities.clear(); self.drafts.clear(); self.budgets.clear(); self.deadlines.clear(); self.reviews.clear()
        for item in restored_data['history']:
            entry = {'type': item['type'], **item}
            if item['type'] == 'opportunity': self.opportunities.append(entry)
            elif item['type'] == 'draft': self.drafts.append(entry)
            elif item['type'] == 'budget': self.budgets.append(entry)
            elif item['type'] == 'deadline': self.deadlines
