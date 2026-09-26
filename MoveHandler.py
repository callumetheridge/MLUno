from Card import *

class MoveHandler:
    def __init__(self, hands: list[list[Card]]):
        self.hands = hands
        self.player_order = [i for i in range(len(hands))]
        self.reversed = False
        
    def is_valid_move(previous_card: Card, next_card: Card, pickup_needed: bool) -> bool:
        if pickup_needed:
            if previous_card.type == CardType.DRAW_TWO:
                return next_card.type == CardType.DRAW_TWO or next_card.type == CardType.WILD_DRAW_FOUR
            
            if previous_card.type == CardType.WILD_DRAW_FOUR:
                return next_card.type == CardType.WILD_DRAW_FOUR
            
        if previous_card.colour == next_card.colour:
            return True
        
        if previous_card.type == next_card.type:
            return True
        
        if next_card.type == CardType.WILD or next_card.type == CardType.WILD_DRAW_FOUR:
            return True
        
        return False
    
    def has_valid_card(prev_card: Card, hand: list[Card], pickup_needed: bool) -> bool:
        for card in hand:
            if MoveHandler.is_valid_move(prev_card, card, pickup_needed):
                return True
            
        return False
        
    def get_additional_pickup_amount(self, previous_card: Card, pickup_on_previous_turn: bool) -> int:
        if pickup_on_previous_turn:
            return 0
            
        if previous_card.get_type() == CardType.DRAW_TWO:
            return 2
        
        if previous_card.get_type() == CardType.WILD_DRAW_FOUR:
            return 4
        
        return 0
    
    def get_next_player_index(self, current_player_index: int, steps: int) -> int:
        if self.reversed:
            return self.player_order[(current_player_index - steps) % len(self.hands)]
        
        return self.player_order[(current_player_index + steps) % len(self.hands)]
        
    def handle_move(self, current_player_index: int, next_card: Card) -> tuple[int, bool]:
        next_card_type = next_card.get_type()
        colour_pick_needed = False
        
        if next_card_type == CardType.REVERSE:
            self.reversed = True
            return self.get_next_player_index(current_player_index, 1), colour_pick_needed
        
        if next_card_type == CardType.SKIP:
            return self.get_next_player_index(current_player_index, 2), colour_pick_needed
        
        if next_card_type == CardType.WILD or next_card_type == CardType.WILD_DRAW_FOUR:
            colour_pick_needed = True
            return self.get_next_player_index(current_player_index, 1), colour_pick_needed
        
        return self.get_next_player_index(current_player_index, 1), colour_pick_needed