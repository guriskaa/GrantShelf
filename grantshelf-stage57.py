# === Stage 57: Add structured result objects for command handlers ===
# Project: GrantShelf
class GrantResult:
    """Structured result returned by grant command handlers."""
    def __init__(self, status: str = "ok", message: str = "", data=None):
        self.status = status
        self.message = message
        self.data = data or {}
    
    @property
    def success(self) -> bool:
        return self.status == "ok"

    def to_dict(self) -> dict:
        result = {"status": self.status, "message": self.message}
        if self.data is not None:
            result["data"] = self.data
        return result

    @classmethod
    def ok(cls, data=None, message="") -> "GrantResult":
        return cls(status="ok", message=message, data=data)

    @classmethod
    def error(cls, message: str) -> "GrantResult":
        return cls(status="error", message=message)

    @classmethod
    def redirect(cls, url: str) -> "GrantResult":
        return cls(status="redirect", message=url)
