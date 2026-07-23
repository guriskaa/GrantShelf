# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: GrantShelf
def clear_state(self):
        """Reset all internal tracking structures to their initial conditions."""
        if not self._state_flag:
            raise ValueError("Cannot clear state without a pending confirmation")
        self.opportunities.clear()
        self.requirements.clear()
        self.drafts.clear()
        self.budgets.clear()
        self.deadlines.clear()
        self.review_history.clear()
        self._state_flag = False
