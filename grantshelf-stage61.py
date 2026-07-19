# === Stage 61: Add performance timing for core list and search operations ===
# Project: GrantShelf
import time, functools

def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        dt = (time.perf_counter() - t0) * 1e3
        print(f"[{func.__name__}] {dt:.2f} ms")
        return result
    return wrapper

class GrantShelf:
    def __init__(self):
        self._opportunities = []
        self._requirements = {}
        self._drafts = {}
        self._budgets = {}
        self._deadlines = {}
        self._reviews = []

    @timed
    def list_opportunities(self, tags=None):
        if not tags:
            return list(self._opportunities)
        return [o for o in self._opportunities if any(t in o.tags for t in tags)]

    @timed
    def search_requirements(self, keyword):
        kw = keyword.lower()
        return {k: v for k, v in self._requirements.items() if kw in str(v).lower()}

    @timed
    def get_draft(self, id_):
        return self._drafts.get(id_)

    @timed
    def set_budget(self, grant_id, amount):
        self._budgets[grant_id] = float(amount)
        return self._budgets[grant_id]

    @timed
    def get_deadline(self, grant_id):
        return self._deadlines.get(grant_id)

    @timed
    def add_review(self, grant_id, score, notes=""):
        self._reviews.append({"grant": grant_id, "score": score, "notes": notes})
