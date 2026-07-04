# === Stage 24: Add grouped summaries by category or status ===
# Project: GrantShelf
def group_summaries(data, key_field='category'):
    groups = {}
    for item in data:
        k = item.get(key_field) or 'Uncategorized'
        if k not in groups:
            groups[k] = {'count': 0, 'total_deadline_days': 0}
        groups[k]['count'] += 1
        days_left = (item['deadline_date'] - datetime.now()).days
        groups[k]['total_deadline_days'] += max(0, days_left)
    return {k: {'items': v['count'], 'avg_days_left': round(v['total_deadline_days']/v['count'], 1)} for k, v in groups.items()}
