# === Stage 55: Add a setting to disable colorized output ===
# Project: GrantShelf
import os

# Disable colorized output when NO_COLOR environment variable is set
if "NO_COLOR" in os.environ:
    os.environ["ANSI_COLORS_DISABLED"] = "1"
