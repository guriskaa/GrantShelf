# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: GrantShelf
class GrantFilter:
    def __init__(self, grants):
        self.grants = grants

    def filter(self, status=None, category=None, owner=None, tag=None):
        result = list(self.grants)
        if status is not None:
            result = [g for g in result if g.get('status') == status]
        if category is not None:
            result = [g for g in result if g.get('category') == category]
        if owner is not None:
            result = [g for g in result if g.get('owner') == owner]
        if tag is not None:
            result = [g for g in result if tag in g.get('tags', [])]
        return result

    def filter_combined(self, **kwargs):
        status = kwargs.pop('status', None)
        category = kwargs.pop('category', None)
        owner = kwargs.pop('owner', None)
        tag = kwargs.pop('tag', None)
        filtered = self.filter(status=status, category=category, owner=owner, tag=tag)
        if not kwargs:
            return filtered
        for key in kwargs:
            val = kwargs[key]
            if callable(val):
                filtered = [g for g in filtered if val(g)]
            else:
                filtered = [g for g in filtered if g.get(key) == val]
        return filtered

    def get_summary(self, status=None, category=None, owner=None, tag=None):
        grants = self.filter(status=status, category=category, owner=owner, tag=tag)
        total = len(grants)
        deadlines = [g for g in grants if 'deadline' in g and g['deadline']]
        urgent = sum(1 for d in deadlines if (d['deadline'] - datetime.now()).days < 30)
        return {'total': total, 'urgent_deadlines': urgent}
