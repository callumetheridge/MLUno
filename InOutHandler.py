from Card import Card
import os
import subprocess

class InOutHandler:
    def __init__(self, hand: list[Card]):
        self.current_hand == hand

        pass

    def print_display_hand(self: list[Card]):
        self.clear()
        for i in range(len(self.current_hand)):
            print(f"{i+1}: ", self.current_hand[i])
        print("Type which card would you like to play: ")

    def clear(self):
        cmd = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
        subprocess.run(cmd, check=False)

    myAge = None
while myAge is None:
    try:
        myAge = int(input("What's your age? "))
    except ValueError:
        print ("Enter an INTEGER, goddammit!!!")

    def take_input(self):
        #stores user's input in a usable way
        try:
            user_input = int(input())
        except ValueError:
            print("bruh enter an integer: ")
        return(self.current_hand[user_input])
        

    def check_input(self):
        pass