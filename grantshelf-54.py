# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: GrantShelf
def colorize(text, color_code):
    """Apply ANSI color codes to text for terminal output."""
    return f"\033[{color_code}m{text}\033[0m"

COLORS = {
    'red': 31,
    'green': 32,
    'yellow': 33,
    'blue': 34,
    'magenta': 35,
    'cyan': 36,
    'white': 37,
}

def print_grant_title(grant):
    """Print a grant entry with colorized title and status."""
    status_colors = {
        'open': ('green', 'Open'),
        'draft': ('yellow', 'Draft'),
        'reviewing': ('magenta', 'Reviewing'),
        'deadline': ('red', 'Deadline Approaching'),
        'approved': ('cyan', 'Approved'),
    }
    status = grant.get('status', 'open')
    color_key, label = status_colors.get(status, ('white', status))
    title = grant['title'] if isinstance(grant, dict) else str(grant)
    print(f"{colorize(title, COLORS[color_key])}  [{label}]")

def print_budget_summary(budget):
    """Print budget details with colorized amounts."""
    total = budget.get('total', 0)
    allocated = budget.get('allocated', 0)
    remaining = total - allocated
    print(f"Total: ${colorize(total, COLORS['cyan']):.2f}")
    print(f"Allocated: ${colorize(allocated, COLORS['green']):.2f} | Remaining: ${colorize(remaining, COLORS['red'] if remaining < 0 else 'green'):.2f}")

def print_deadline_alert(deadlines):
    """Print deadline information with colorized urgency."""
    for deadline in deadlines:
        days_left = deadline.get('days_remaining', 0)
        if days_left <= 7:
            print(f"⚠️ {colorize(deadline['description'], COLORS['red'])} - {days_left} days left")
        elif days_left <= 30:
            print(f"📅 {deadline['description']} - {days_left} days left")
        else:
            print(f"✅ {deadline['description']} - {days_left} days left")
