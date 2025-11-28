from datetime import datetime

class Event:
    id: int
    title: str
    description: str
    date: datetime
    location: str
    
    def __init__(self, id, title, description, date, location):
        self.id = id
        self.title = title
        self.description = description
        self.date = date
        self.location = location
        
    def __str__(self)->str:
        return self.title
    
    def to_dict(self)->dict:
        dictionary = {
            "year": self.date.year,
            "month": self.date.month,
            "day": self.date.day,
            "hour": self.date.hour,
            "minutes": self.date.minute
        }
        return dictionary
    
        