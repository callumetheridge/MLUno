from Card import *

class MoveManager:
    def __init__(self, hands: list[list[Card]], player_order: list[Card]):
        self.hands = hands
        self.player_order = player_order
        
    def handle_move(self) -> tuple[list[list[Card]], int, int]:
        # Return the hands, next player number, number of cards to be picked up
        pass