# === Stage 44: Add backup creation for the data file ===
# Project: GrantShelf
def create_backup(data_file, backup_dir="."):
    """Create a timestamped backup of the grant data file."""
    import shutil, os
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    base = backup_dir + "/grantshelf_backup_"
    counter = 1
    while os.path.exists(base + str(counter)):
        counter += 1
    backup_path = base + str(counter)
    shutil.copy2(data_file, backup_path)
    print(f"Backup saved to {backup_path}")
