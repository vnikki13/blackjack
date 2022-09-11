class Hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card):
        self.cards.append(card)

    def display(self):
        print(f'''{"Dealer's" if self.dealer else "Your"} Hand:''')
        for card in self.cards:
            print(card)

        # Use formatting for UI spacing
        print()
