from enum import Enum

class CardType(Enum):
    ZERO = 0 
    ONE = 1 
    TWO = 2 
    THREE = 3 
    FOUR = 4 
    FIVE = 5 
    SIX = 6 
    SEVEN = 7 
    EIGHT = 8 
    NINE = 9
    REVERSE = 10 
    SKIP = 11
    DRAW_TWO = 12
    CHANGE_COLOUR = 13
    DRAW_FOUR = 14
    
    def __str__(self) -> str:
        return self.name