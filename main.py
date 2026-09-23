from DeckBuilder import DeckBuilder
from Dealer import Dealer

def main():
    deck_builder = DeckBuilder()
    deck_builder.shuffle_deck()
    dealer = Dealer(deck_builder.get_deck(), 3)
    dealer.print_hands()

if __name__ == "__main__":
    main()