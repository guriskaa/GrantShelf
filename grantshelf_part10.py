# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: GrantShelf
class SearchFilter:
    def __init__(self, data):
        self.data = data
    
    def search(self, query):
        if not query.strip():
            return list(self.data)
        
        q_lower = query.lower()
        results = []
        for item in self.data:
            searchable_text = (item.get('title', '') + ' ' + 
                              item.get('description', '') + ' ' + 
                              item.get('requirements', '')).lower()
            
            if q_lower in searchable_text or any(q_lower == word.lower() for word in searchable_text.split()):
                results.append(item)
        
        return results
