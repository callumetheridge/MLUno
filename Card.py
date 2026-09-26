from CardType import *
from CardColour import *

class Card:
    BLUE   = "\033[1;34m"
    GREEN  = "\033[1;32m"
    RED    = "\033[1;31m"
    YELLOW = "\033[1;93m"
    WHITE  = "\033[1;37m"
    RESET  = "\033[0m"
    
    def __init__(self, type: CardType, colour: CardColour):
        self.type = type
        self.colour = colour
        
    def print_in_colour(text: str, colour: str):
        print(f"{colour}{text}{Card.RESET}")
    
    def get_console_colour(self):
        if self.colour == CardColour.BLUE:
            return Card.BLUE
        
        if self.colour == CardColour.GREEN:
            return Card.GREEN
        
        if self.colour == CardColour.RED:
            return Card.RED
        
        if self.colour == CardColour.YELLOW:
            return Card.YELLOW
        
        if self.colour == CardColour.WILD:
            return Card.WHITE
        
    def get_colour(self):
        return self.colour
    
    def get_type(self):
        return self.type
    
    def set_colour(self, colour: CardColour):
        self.colour = colour
    
    def __str__(self) -> str:
        return f"{self.get_console_colour()}{str(self.type).replace("_", " ")}{self.RESET}"