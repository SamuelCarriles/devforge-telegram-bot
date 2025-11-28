from datetime import datetime

class Task:
 
 id: int
 title: str
 description: str
 due_date: datetime
 completed: bool
 create_at: datetime
 completed_at: datetime

 def __init__(self, id, title, description=None, due_date=None, completed=False, created_at=None, completed_at=None):
   self.id=id
   self.title=title
   self.description=description
   self.due_date=due_date
   self.completed=completed
   self.create_at=completed_at
   self.completed_at=completed_at
  
