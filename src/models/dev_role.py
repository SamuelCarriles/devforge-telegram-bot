class DevRole:
    key: str
    name: str
    icon: str
    
    def __init__(self, key: str, name: str, icon: str ):
        self.key = key
        self.name = name
        self.icon = icon
        
    def __str__(self) -> str:
        return f"{self.icon} {self.name}"
    
    