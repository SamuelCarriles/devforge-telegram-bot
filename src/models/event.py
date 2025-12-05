from datetime import datetime
from pydantic import BaseModel

days = [
    "Lunes", "Martes", "Miércoles", "Jueves",
    "Viernes", "Sábado", "Domingo"
    ]

months = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
        

class Event(BaseModel):
    id: int
    title: str
    description: str
    date: datetime
    location: str
    
    def is_upcoming(self)-> bool:
        return self.date > datetime.now()
    
    def format_date(self) -> str:
        
        day = days[self.date.weekday()]
        month = months[self.date.month - 1]
        
        return self.date.strftime(f"{day} %d de {month}, %I:%M %p")
        