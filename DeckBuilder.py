from CardType import CardType
from CardColour import CardColour
from Card import Card
import random

class DeckBuilder:
    def __init__(self):
        self.deck = []
        self.deck_dict = {type: 2 for type in CardType}
        
        self.deck_dict[CardType.ZERO] = 1
        del self.deck_dict[CardType.CHANGE_COLOUR]
        del self.deck_dict[CardType.DRAW_FOUR]
        
        self.initialise_deck()
        
    def initialise_deck(self):
        for colour in CardColour:
            if colour == CardColour.WILD: 
                continue
            
            for type, number in self.deck_dict.items():
                self.add_cards_to_deck(type, colour, number)
                
        self.add_cards_to_deck(CardType.CHANGE_COLOUR, CardColour.WILD, 4)
        self.add_cards_to_deck(CardType.DRAW_FOUR, CardColour.WILD, 4)
    
    def add_cards_to_deck(self, type: CardType, colour: CardColour, number: int):
        for _ in range(number):
            self.deck.append(Card(type, colour))
            
    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def print_deck(self):
        for card in self.deck:
            print(card)

    def print_deck_size(self):
        print(len(self.deck))
    
    def get_deck(self) -> dict[CardColour, int]:
        return self.deck