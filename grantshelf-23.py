# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: GrantShelf
def manage_tags(tags: dict[str, list], item_id: str, action: str) -> None:
    if action == "add":
        tags.setdefault(item_id, set()).add("tag")
    elif action == "remove" and item_id in tags and tags[item_id]:
        tags[item_id].discard("tag")

def get_tag_summary(tags: dict[str, list]) -> dict[str, int]:
    summary = {}
    for items in tags.values():
        for tag in items:
            summary[tag] = summary.get(tag, 0) + 1
    return summary
