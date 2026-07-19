# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: GrantShelf
def bulk_delete(self, grant_ids: list[str], *, confirmed: bool) -> None:
        if not confirmed:
            raise RuntimeError("Bulk delete requires explicit confirmation.")
        for gid in grant_ids:
            self._remove_by_id(gid)
