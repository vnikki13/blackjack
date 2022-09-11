from card import Card

suits = [ 'Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = [
    {"rank": "A", "value": 11},
    {"rank": "2", "value": 2},
    {"rank": "3", "value": 3},
    {"rank": "4", "value": 4},
    {"rank": "5", "value": 5},
    {"rank": "6", "value": 6},
    {"rank": "7", "value": 7},
    {"rank": "8", "value": 8},
    {"rank": "9", "value": 9},
    {"rank": "10", "value": 10},
    {"rank": "J", "value": 10},
    {"rank": "Q", "value": 10},
    {"rank": "K", "value": 10}
]

cards = []

for suit in suits:
    for rank in ranks:
        card = Card(rank, suit)
        cards.append(card)

for card in cards:
    print(card)
