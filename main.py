from DeckBuilder import *
from Dealer import *
from InOutHandler import *
from GameManager import *

def main():
    player_count = 2
    game_manager = GameManager(player_count)
    game_manager.run_game()

if __name__ == "__main__":
    main()