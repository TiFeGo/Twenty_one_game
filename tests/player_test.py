import pytest
from context import src
from src.card import Card
from src.player import Player


def test_additional():
    player = Player(("", 0))
    player.add_card(card=Card("Ace", ""))
    player.add_card(card=Card("Ace", ""))
    player.add_card(card=Card("Ace", ""))
    player.add_card(card=Card("Jack", ""))
    assert player.score == 15


def test_display():
    player = Player(("", 0))
    player.add_card(card=Card("Ace", ""))
    player.add_card(card=Card("Ace", ""))
    player.add_card(card=Card("Ace", ""))
    player.add_card(card=Card("Jack", ""))
    function_result = player.display_card()
    expect = 'value: Ace, suit:   value: Ace, suit:   value: Ace, suit:   value: Jack, ' \
             'suit:   '
    assert function_result == expect
