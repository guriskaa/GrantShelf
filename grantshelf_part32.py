# === Stage 32: Add pagination helpers for long console output ===
# Project: GrantShelf
def paginate(data, page_size=10):
    """Yield chunks of size *page_size* from *data*."""
    for i in range(0, len(data), page_size):
        yield data[i:i+page_size]
