# === Stage 35: Add active user switching and user-specific records ===
# Project: GrantShelf
class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'<User {self.name}>'

class GrantShelf:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.records = {}
    def add_user(self, user):
        self.users[user.name] = user
    def switch_user(self, name):
        if name not in self.users:
            raise KeyError(f'User {name!r} is not registered.')
        self.current_user = self.users[name]
    @property
    def active_user(self):
        return self.current_user or None
    def record(self, key, value):
        if self.active_user is None:
            raise RuntimeError('No user is currently active; call switch_user() first.')
        path = (self.active_user.name, key)
        self.records[path] = value
    @property
    def records_for(self, user_name):
        return {k: v for k, v in self.records.items() if k[0] == user_name}
