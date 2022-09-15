from src.game import Game
from src.game import Hand
from src.card import Card

def test_game_class_is_initiated_with_correct_attributes():
    game = Game()   
    assert(len(game.deck.cards) == 52)
    assert(type(game.player_hand) is Hand)
    assert(type(game.dealer_hand) is Hand)
    assert(game.player_hand.dealer is False)
    assert(game.dealer_hand.dealer is True)

def test_hands_have_two_cards_when_deal_hands():
    game = Game()

    assert(len(game.player_hand.cards) == 0)
    assert(len(game.dealer_hand.cards) == 0)

    game.deal_hands()

    assert(len(game.player_hand.cards) == 2)
    assert(len(game.dealer_hand.cards) == 2)

def test_game_is_over_if_player_has_blackjack(capfd):
    game = Game()

    cards = [
        Card({"rank": "A", "value": 11}, 'Spades'), 
        Card({"rank": "J", "value": 10}, 'Spades')
    ]
    game.player_hand.cards = cards
    assert(game.player_hand.cards == cards)

    result = game.is_winner()
    out, err = capfd.readouterr()
    assert(out == "You got blackjack 🥳\n")
    assert(result is True)
