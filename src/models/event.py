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
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "date": self.date.isoformat(),
            "location": self.location
        }
        return dictionary
    
    
        
        
        
    
        