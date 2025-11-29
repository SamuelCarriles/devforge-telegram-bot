class BotRol:
    def to_dict(self): ...

    @classmethod
    def from_dict(cls, data: dict):
        return cls()

    def can_access_command(self, command: str) -> bool: ...
