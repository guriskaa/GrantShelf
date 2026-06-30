# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: GrantShelf
class CommandDispatcher:
    def __init__(self, handlers):
        self.handlers = {cmd.lower(): handler for cmd, handler in handlers.items()}

    def dispatch(self, text):
        if not text.strip(): return None
        parts = text.split(maxsplit=1)
        if not parts: return None
        command = parts[0]
        args = parts[1].strip() if len(parts) > 1 else ""
        handler = self.handlers.get(command)
        if handler is None:
            print(f"Unknown command: {command}")
            return None
        try:
            result = handler(args)
            if callable(result):
                result()
            elif isinstance(result, str):
                print(result)
            else:
                print(result)
        except Exception as e:
            print(f"Error executing '{command}': {e}")
