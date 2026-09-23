from CardType import CardType
from CardColour import CardColour
from Card import Card

class DeckBuilder:
    def __init__(self):
        self.deck = []
        self.deck_dict = {type: 2 for type in CardType}
        
        self.deck_dict[CardType.ZERO] = 1
        del self.deck_dict[CardType.WILD]
        del self.deck_dict[CardType.WILD_DRAW_FOUR]
        
        self.initialise_deck()
        
    def initialise_deck(self):
        for colour in CardColour:
            if colour == CardColour.WILD: 
                continue
            
            for type, number in self.deck_dict.items():
                self.add_cards_to_deck(type, colour, number)
                
        self.add_cards_to_deck(CardType.WILD, CardColour.WILD, 4)
        self.add_cards_to_deck(CardType.WILD_DRAW_FOUR, CardColour.WILD, 4)
    
    def add_cards_to_deck(self, type: CardType, colour: CardColour, number: int):
        for _ in range(number):
            self.deck.append(Card(type, colour))
    
    def print_deck(self):
        for card in self.deck:
            print(card)
    
    def get_deck(self) -> dict[CardColour, int]:
        return self.deck