from deck import Deck

deck = Deck()
deck.shuffle()

for card in deck.cards:
    print(card)
