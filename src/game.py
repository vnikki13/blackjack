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

    def is_winner(self, game_over = False):
        player_hand_value = self.player_hand.get_value()
        dealer_hand_value = self.dealer_hand.get_value()

        player_has_blackjack = self.player_hand.is_blackjack()
        dealer_has_blackjack = self.dealer_hand.is_blackjack()

        if not game_over:
            if player_hand_value > 21:
                print("Greater than 21 you busted 😭 ")
                return True
            elif dealer_hand_value > 21:
                print("Dealer busted, you win 🥳 ")
                return True
            elif dealer_has_blackjack and player_has_blackjack:
                print("Both players have blackjack! Tie! 😬 ")
                return True
            elif dealer_has_blackjack:
                print("Dealer got blackjack 😭 ")
                return True
            elif player_has_blackjack:
                print("You got blackjack 🥳")
                return True
        else:
            if player_hand_value > dealer_hand_value:
                print("You win 🥳 ")
            elif player_hand_value == dealer_hand_value:
                print("Tie 😬 ")
            else:
                print("Dealer wins 😭 ")
        return False

    def play(self):
        print("\n♠️ ♥️  Welcome to Blackjack  ♣️ ♦️\n")

        self.deal_hands()
        self.display_hands()

        # Player chooses to Hit or Stand if there is no initial winner
        choice = ''
        while not self.is_winner() and choice not in ['s', 'stand']:
            choice = input("Would you like to 'Hit' or 'Stand'? => ").lower()
            # Formatting for UI spacing
            print()
            while choice not in ['h', 'hit', 's', 'stand']:
                choice = input("Please enter 'Hit', or 'Stand', (H/S)\n").lower()

            if choice in ['h', 'hit']:
                self.player_hand.add_card(self.deck.deal())
                self.player_hand.display()

        # Dealer needs to equal or be over 17 points
        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.deal())

        self.dealer_hand.display(True)

        self.is_winner(True)

Game().play()
