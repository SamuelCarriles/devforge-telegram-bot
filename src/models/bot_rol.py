from src.logic.commands import clean_command
class BotRol:
    key: str
    name: str
    hierarchy: int
    allowed_commands: list[str]

    def __init__(self, key: str, name: str, hierarchy: int, allowed_commands: list[str]) -> None:
        self.key = key
        self.name = name
        self.hierarchy = hierarchy
        self.allowed_commands = clean_command(allowed_commands) 
    
    def __str__(self) -> str:
        return self.name
    
    def can_access_command(self, command: str) -> bool:
        comm = clean_command(command)[0]

        if comm in self.allowed_commands:
            return True
        
        return False