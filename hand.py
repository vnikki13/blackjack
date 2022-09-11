class Hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card):
        self.cards.append(card)

    def display(self, show_all_dealer_cards=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} Hand:''')
        for i, card in enumerate(self.cards):
            if self.dealer and i == 0 and not show_all_dealer_cards:
                print("** Hidden **")
            else:
                print(card)

        # Use formatting for UI spacing
        print()

    def get_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            self.value += int(card.rank["value"])
            if (card.rank["rank"] == "A"):
                has_ace = True

            if has_ace and self.value > 21:
                self.value -= 10

        return self.value

    def is_blackjack(self):
        return True if self.get_value() == 21 else False
