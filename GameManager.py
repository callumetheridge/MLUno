from Card import *
from Dealer import *
from CardColour import *
from InOutHandler import *
from MoveHandler import *

class GameManager:
    def __init__(self, player_count: int):
        deck_builder = DeckBuilder()
        self.dealer = Dealer(deck_builder, player_count)
        self.player_count = self.dealer.get_player_count()

    def play_card(self, card: Card, player_number: int):
        pass
        
    def handle_pickups(self):
        pass
    
    def increment_player_index(self, current_player_index: int) -> int:
        return (current_player_index + 1) % self.player_count
    
    def run_game(self):
        hands = self.dealer.get_hands()
        previous_card = self.dealer.get_first_card()
        placed_cards = [previous_card]
        
        running = True
        pickup_on_previous_turn = False
        current_player_index = 0
        pickup_count = 0
        
        in_out_handler = InOutHandler()
        move_handler = MoveHandler(hands)
        
        while running:
            previous_card = placed_cards[-1]
            pickup_count += move_handler.get_additional_pickup_amount(previous_card, pickup_on_previous_turn)
            pickup_needed = pickup_count != 0
            has_valid_card = MoveHandler.has_valid_card(previous_card, hands[current_player_index], pickup_needed)
            
            if not has_valid_card:
                self.dealer.pickup_cards(pickup_count if pickup_count != 0 else 1, current_player_index)
                in_out_handler.show_pickup(hands[current_player_index], pickup_count if pickup_count != 0 else 1, current_player_index + 1)
                current_player_index = self.increment_player_index(current_player_index)
                
                if pickup_count != 0:
                    pickup_on_previous_turn = True
                    pickup_count = 0
                    
                continue
            
            next_card = in_out_handler.get_next_card(hands[current_player_index], previous_card, current_player_index + 1, False)
            hands[current_player_index].remove(next_card)
            placed_cards.append(next_card)
            pickup_on_previous_turn = False
            pickup_count = 0    
            current_player_index, colour_pick_needed = move_handler.handle_move(current_player_index, next_card)
            
            if colour_pick_needed:
                next_card.set_colour(in_out_handler.get_colour_choice())