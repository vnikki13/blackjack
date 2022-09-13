from src.card import Card

def test_a_card_class_is_created():
    card = Card({}, '')
    assert(type(card) is Card)
    assert(card.rank == {})

def test_a_card_is_printed_correctly():
    card = Card({"rank": "A", "value": 11}, "Heart")
    assert (type(card) is Card)
    print(card)
    assert (str(card) == "A of Heart")
