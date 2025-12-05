from datetime import datetime
from .record import Record
from .bot_rol import BotRol, Guest
from .dev_role import DevRole
from typing import Self
from pydantic import BaseModel


class User(BaseModel):
    """
    Clase para representar a los usuarios del bot
    """
    
    telegram_id: str
    username: str
    name: str
    bot_rol: BotRol
    record: Record | None
    joined_at: datetime
    dev_rol: DevRole 

    def __str__(self) -> str:
        return self.name

    def have_permission(self, command: str) -> bool:
        """Comprueba si el usuario tiene permiso de ejecutar un comando

        Args:
            command (str): El comando que se desea comprobar

        Returns:
            bool: Devuelve `True` o `False` en dependencia de si el usuario tiene permiso o no
        """
        return self.bot_rol.can_access_command(command)
