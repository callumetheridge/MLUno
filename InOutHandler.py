from Card import *
from CardColour import *
from MoveHandler import *
import os
import subprocess

class InOutHandler:
    BLUE   = "\033[1;34m"
    GREEN  = "\033[1;32m"
    RED    = "\033[1;31m"
    YELLOW = "\033[1;93m"
    WHITE  = "\033[1;37m"
    RESET  = "\033[0m"
    
    def print_in_colour(self, text: str, colour: str):
        print(f"{colour}{text}{InOutHandler.RESET}")

    def get_next_card(self, current_hand: list[Card], previous_card: Card, current_player_number: int, pickup_needed: bool) -> Card:
        InOutHandler.clear_terminal()
        self.print_in_colour(f"Player {current_player_number + 1}'s turn", self.WHITE)
        print(f"Previous card: {previous_card}")        
        InOutHandler.print_hand(current_hand)
            
        return self.get_card_input(current_hand, previous_card, pickup_needed)
    
    def show_pickup(self, current_hand: list[Card], pickup_count: int, current_player_number: int):
        InOutHandler.clear_terminal()
        self.print_in_colour(f"Player {current_player_number} has picked up {pickup_count} cards", self.WHITE)
        InOutHandler.print_hand(current_hand)
        print("Press enter to continue: ", end="")
        input()

    def clear_terminal():
        command = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
        subprocess.run(command, check=False)
        
    def print_hand(current_hand: list[int]):
        for i in range(len(current_hand)):
            print(f"{i + 1}: ", current_hand[i])

    def get_card_input(self, current_hand: list[Card], previous_card: Card, pickup_needed: bool) -> Card:
        user_input = None
        getting_input = True
        
        while getting_input:
            print("Select card: ", end="")
            
            try:
                user_input = int(input())
                
                if user_input > len(current_hand) or user_input <= 0:
                    raise ValueError
                
                if not MoveHandler.is_valid_move(previous_card, current_hand[user_input - 1], pickup_needed):
                    raise ValueError
                
                getting_input = False
                
            except ValueError:
                print("Invalid input")
            
        return current_hand[user_input - 1]
    
    def get_colour_choice(self):
        self.print_in_colour("\nSelect a colour for the wild card:", self.WHITE)
        print("1: ", end="")
        self.print_in_colour("Blue", self.BLUE)
        print("2: ", end="")
        self.print_in_colour("Green", self.GREEN)
        print("3: ", end="")
        self.print_in_colour("Red", self.RED)
        print("4: ", end="")
        self.print_in_colour("Yellow", self.YELLOW)
        
        user_input = None
        getting_input = True
        colours = [CardColour.BLUE, CardColour.GREEN, CardColour.RED, CardColour.YELLOW]
        
        while getting_input:
            print("Select colour: ", end="")
            
            try:
                user_input = int(input())
                
                if user_input < 1 or user_input > 4:
                    raise ValueError
                
                getting_input = False
            
            except ValueError:
                print("Invalid input")
                
        return colours[user_input - 1]