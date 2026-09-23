from enum import Enum

class CardColour(Enum):
    BLUE = 1
    GREEN = 2
    RED = 3
    YELLOW = 4
    WILD = 5
    
    def __str__(self) -> str:
        return self.name