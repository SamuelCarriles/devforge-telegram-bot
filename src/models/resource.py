from datetime import datetime
from typing import Self
from uuid import uuid4
from pydantic import BaseModel

class Resource(BaseModel):
    id: str
    title: str
    url: str
    category: str
    added_by: str
    added_at: datetime
        
    def __str__(self) -> str:
        return self.title
    
    def format_link(self) -> str:
        return (f"[{self.title}]({self.url})")
    