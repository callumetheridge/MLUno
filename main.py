from DeckBuilder import *
from Dealer import *
from InOutHandler import *

def main():
    deck_builder = DeckBuilder()
    deck_builder.shuffle_deck()
    dealer = Dealer(deck_builder.get_deck(), 5)
    inoutHandler = InOutHandler()
    inoutHandler.get_next_card(dealer.get_hands()[0])

if __name__ == "__main__":
    main()