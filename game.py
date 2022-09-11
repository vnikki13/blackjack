from deck import Deck
from hand import Hand

class Game:
    def __init__(self):  
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand(True)

    def deal_hands(self):
        for x in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

    def display_hands(self):
            self.dealer_hand.display()
            self.player_hand.display()

    def play(self):
        self.deal_hands()
        self.display_hands()

Game().play()
