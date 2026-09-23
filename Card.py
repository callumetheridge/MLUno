from CardType import CardType
from CardColour import CardColour

class Card:
    def __init__(self, type: CardType, colour: CardColour):
        self.type = type
        self.colour = colour
        
    def __str__(self) -> str:
        return f"{self.colour} {self.type}"