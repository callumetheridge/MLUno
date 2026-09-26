from Card import *
from DeckBuilder import *

class Dealer:
    def __init__(self, deck_builder: DeckBuilder, player_count: int):
        self.hand_size = 7
        self.max_players = 10
        self.deck = deck_builder.get_deck()
        self.player_count = self.max_players if player_count > self.max_players else player_count
        self.hands = self.get_dealt_hands()
       
    def get_player_count(self) -> int:
        return self.player_count

    def get_dealt_hands(self) -> list[list[Card]]:
        hands = [[] for _ in range(self.player_count)]
        
        for _ in range(self.hand_size):
            for i in range(self.player_count):
                hands[i % self.player_count].append(self.get_next_card())
                
        return hands

    def get_next_card(self) -> Card:
        return self.deck.pop()
    
    def get_first_card(self) -> Card:
        card = self.deck.pop()
        
        while card.type.value > 9:
            card = self.deck.pop()
            
        return card
    
    def pickup_cards(self, amount: int, current_player_index: int):
        for _ in range(amount):
            self.hands[current_player_index].append(self.get_next_card())

    def print_hands(self):
        for i in range(self.player_count):
            line = ""
            
            for j in range(len(self.hands[i])):
                line += f"{self.hands[i][j]}, "
                
            print(line[:-2])

    def get_hands(self):
        return self.hands
    
    def get_deck(self):
        return self.deck