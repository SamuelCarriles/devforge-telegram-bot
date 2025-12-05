from src.logic.commands import parse_command
from src.utils.command_permissions import COMMAND_ALLOWLIST
from pydantic import BaseModel

class BotRol(BaseModel):
    key: str
    name: str
    hierarchy: int
    min_rank_required: int
    
    def __str__(self) -> str:
        return self.name
    
    def can_access_command(self, command: str) -> bool:
        comm = parse_command(command)[0]
        print(comm)
        if comm in COMMAND_ALLOWLIST and self.key in COMMAND_ALLOWLIST[comm]:
            return True
        return False

class Admin(BotRol):
        key="admin", 
        name="Administrador", 
        hierarchy=100,
        min_rank_required=1300
 
class Member(BotRol):
        key="member", 
        name="Miembro", 
        hierarchy=25,
        min_rank_required=0

class Guest(BotRol):
        key="guest", 
        name="Invitado", 
        hierarchy=1,
        min_rank_required=0
