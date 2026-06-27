# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: GrantShelf
def delete_grant(grant_id: int, confirm: bool = True) -> None | str:
    if grant_id in grants_db:
        entry = grants_db[grant_id]
        if confirm or input(f"Удалить грант {entry['title']}? (y/n): ").lower() != 'y':
            return "Операция отменена."
        del grants_db[grant_id]
        print(f"Грант {grant_id} удален.")
    else:
        return f"Грант с ID {grant_id} не найден."
