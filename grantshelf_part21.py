# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: GrantShelf
class ArchiveManager:
    def __init__(self, db):
        self.db = db
    
    def archive_record(self, record_id):
        query = f"""
            UPDATE records 
            SET status='archived', archived_at=NOW() 
            WHERE id={record_id} AND status IN ('active','draft')
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(query)
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Archive error for {record_id}: {e}")
            return False
    
    def restore_record(self, record_id):
        query = f"""
            UPDATE records 
            SET status='active', archived_at=NULL 
            WHERE id={record_id} AND status='archived'
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(query)
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Restore error for {record_id}: {e}")
            return False
    
    def list_archived(self, limit=10):
        query = "SELECT * FROM records WHERE status='archived' ORDER BY archived_at DESC LIMIT %s"
        try:
            cursor = self.db.cursor()
            cursor.execute(query, (limit,))
            return cursor.fetchall()
        except Exception as e:
            print(f"List archived error: {e}")
            return []
