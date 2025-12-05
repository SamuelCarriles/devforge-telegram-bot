from typing import Self
from pydantic import BaseModel

class DevRole(BaseModel):
    key: str
    name: str
    icon: str

class Backend(DevRole):
        key = "backend", 
        name = "Backend Developer", 
        icon = "⚙️"
        
class Frontend(DevRole):
            key = "frontend", 
            name = "Frontend Developer", 
            icon = "🎨"
        
class Tester(DevRole):
            key = "tester", 
            name = "QA Tester", 
            icon = "🧪"
        
class DevOps(DevRole):
            key = "devops", 
            name = "DevOps Engineer", 
            icon = "☁️"

        
        

        

        

        