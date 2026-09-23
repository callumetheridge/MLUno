from DeckBuilder import DeckBuilder
from Dealer import Dealer
from InOutHandler import InOutHandler

def main():
    deck_builder = DeckBuilder()
    deck_builder.shuffle_deck()
    # deck_builder.print_deck_size()
    dealer = Dealer(deck_builder.get_deck(), 5)
    # dealer.print_hands()
    # deck_builder.print_deck_size()
    inoutHandler = InOutHandler()
    inoutHandler.print_display_hand(dealer.get_hands()[1])

if __name__ == "__main__":
    main()