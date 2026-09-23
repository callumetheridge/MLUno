from Card import Card
from CardColour import CardColour

class GameManager:
    def __init__(self, player_number: int, deck: list[Card], hands: list[list[Card]]):
        self.player_number = player_number
        self.deck = deck
        self.hands = hands

    def play_card(self, card: Card, player_number: int):
        pass
        
    def check_move(prev_card: Card, next_card: Card) -> bool:
        if prev_card.colour == next_card.colour or next_card.colour == CardColour.WILD: 
            return True
        
        if prev_card.type == next_card.type:
            return True
        
        return False
        
    def handle_pickups(self):
        pass
    
    def run_game(self):
        running = True
        current_player_num = 0
        additional_pickups = 0
        
        while running:
            # Player picks card to play
            # Check if card can be played
            # If card cannot be played retry
            # Add card to the played deck
            # If special card update order / pickups / colour changes
            #      - skip, reverse, wildcard, +2/+4
            # 
            # Increment player number
            
            pass