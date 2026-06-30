# === Stage 16: Add argparse support for the most common commands ===
# Project: GrantShelf
import argparse

def main():
    parser = argparse.ArgumentParser(description="GrantShelf CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # List opportunities
    list_parser = subparsers.add_parser("list", help="List all grant opportunities")
    list_parser.add_argument("--status", choices=["open", "closed"], default="open", help="Filter by status")
    
    # Create new opportunity
    create_parser = subparsers.add_parser("create", help="Create a new opportunity")
    create_parser.add_argument("-n", "--name", required=True, help="Grant name")
    create_parser.add_argument("-d", "--deadline", help="Submission deadline (YYYY-MM-DD)")
    
    # View details
    view_parser = subparsers.add_parser("view", help="View opportunity details")
    view_parser.add_argument("id", type=int, help="Opportunity ID")
    
    # Add review note
    add_parser = subparsers.add_parser("add-review", help="Add a review note to an opportunity")
    add_parser.add_argument("id", type=int, help="Opportunity ID")
    add_parser.add_argument("-m", "--message", required=True, help="Review text")

if __name__ == "__main__":
    args = parser.parse_args()
    if hasattr(args, "command"):
        print(f"Executing command: {args.command}")
        # Placeholder for actual logic implementation based on parsed arguments
