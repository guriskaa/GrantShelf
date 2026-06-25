# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: GrantShelf
def validate_identifier(value: str) -> bool:
    if len(value) < 3 or len(value) > 50:
        return False
    if value != value.lower():
        return False
    for char in value:
        if not (char.isalnum() or char == '-'):
            return False
    return True

def validate_short_text(value: str, max_len: int = 200) -> bool:
    if len(value.strip()) < 10:
        return False
    if len(value) > max_len:
        return False
    for char in value:
        if not (char.isalnum() or ' '.startswith(char) and char.isspace()):
            continue
        if not (char.isascii() and char in string.ascii_letters + string.digits + ' \n.,!?'):
            return False
    return True

def validate_required_field(value: str, field_name: str = '') -> bool:
    if value is None or value == '' or value.strip() == '':
        raise ValueError(f"Required field '{field_name}' cannot be empty")
    return True
