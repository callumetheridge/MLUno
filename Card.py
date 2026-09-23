from CardType import *
from CardColour import *

class Card:
    def __init__(self, type: CardType, colour: CardColour):
        self.type = type
        self.colour = colour
        
    def __str__(self) -> str:
        return f"{self.colour} {self.type}"