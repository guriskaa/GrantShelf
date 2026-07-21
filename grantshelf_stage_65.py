# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: GrantShelf
def merge_imports(existing, new_block):
    """Merge a new code block into existing content while avoiding obvious duplicates."""
    if not new_block.strip():
        return existing
    
    # Strip whitespace from both for comparison
    normalized_existing = existing.strip()
    normalized_new = new_block.strip()
    
    # If the entire new block is already in the existing text, skip it
    if normalized_new in normalized_existing:
        return existing
    
    # Check if the first line of the new block (stripped) exists as a standalone 
    # or part of an import statement at the end of existing content
    first_line = new_block.split('\n')[0].strip()
    
    # Simple heuristic: check if last few lines of existing match the start of new
    lines_existing = normalized_existing.split('\n')
    lines_new = normalized_new.split('\n')
    
    overlap_start = 0
    for i in range(min(len(lines_new), 5)):  # Check first 5 lines of new block
        if (lines_existing[-(i+1)].strip() == lines_new[i].strip()):
            overlap_start = i + 1
    
    # If there's an overlap at the end, keep only the non-overlapping part
    if overlap_start > 0:
        return existing + '\n' + '\n'.join(lines_new[overlap_start:])
    
    return existing + new_block
