from Card import *
import os
import subprocess

class InOutHandler:
    def __init__(self):
        pass

    def get_next_card(self, current_hand: list[Card]) -> Card:
        self.clear_terminal()
        
        for i in range(len(current_hand)):
            print(f"{i + 1}: ", current_hand[i])
            
        return self.get_card_input(current_hand)

    def clear_terminal(self):
        command = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
        subprocess.run(command, check=False)

    def get_card_input(self, current_hand: list[Card]) -> Card:
        user_input = None
        getting_input = True
        
        while getting_input:
            print("Select card: ", end="")
            
            try:
                user_input = int(input())
                
                if user_input > len(current_hand) or user_input <= 0:
                    raise ValueError
                
                getting_input = False
                
            except ValueError:
                print("Invalid input")
            
        return current_hand[user_input - 1]