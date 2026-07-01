# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: GrantShelf
def dry_run_mode():
    import sys, os
    if len(sys.argv) > 1 and sys.argv[1] == "--dry-run":
        old_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
        try:
            yield
        finally:
            sys.stdout.close()
            sys.stdout = old_stdout
    else:
        yield

def safe_write(path, content):
    if "--dry-run" in sys.argv:
        print(f"[DRY-RUN] Would write to {path}:")
        for line in content.splitlines():
            print(line)
        return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

def safe_delete(path):
    if "--dry-run" in sys.argv:
        print(f"[DRY-RUN] Would delete {path}")
        return False
    os.remove(path)
    return True
