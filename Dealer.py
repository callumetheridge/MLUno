from Card import *

class Dealer:
    def __init__(self, deck: list[Card], player_count: int):
        self.hand_size = 7
        self.max_players = 10
        self.deck = deck
        self.player_count = 10 if player_count > self.max_players else player_count 
        self.hands = [[] for _ in range(self.player_count)]
        self.deal_cards()

    def deal_cards(self):
        for _ in range(self.hand_size):
            for i in range(self.player_count):
                self.hands[i % self.player_count].append(self.get_next_card())

    def get_next_card(self):
        return self.deck.pop()

    def print_hands(self):
        for i in range(self.player_count):
            line = ""
            
            for j in range(len(self.hands[i])):
                line += f"{self.hands[i][j]}, "
                
            print(line[:-2])

    def get_hands(self):
        return self.hands