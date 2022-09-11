from deck import Deck
from hand import Hand

deck = Deck()
deck.shuffle()

player_hand = Hand()
dealer_hand = Hand(True)

player_hand.add_card(deck.deal())
dealer_hand.add_card(deck.deal())

dealer_hand.display()
player_hand.display()
