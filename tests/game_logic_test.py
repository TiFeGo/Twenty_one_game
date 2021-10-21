import pytest
from context import src
from src.card import Card
from src.game_logic import GameLogic
from src.player import Player

game_logic = GameLogic()


def test_win_logic():
    player1 = Player(("", 0))
    player2 = Player(("", 0))
    player3 = Player(("", 0))
    player4 = Player(("", 0))

    player1.add_card(Card("Ace", ""))
    player1.add_card(Card(10, ""))

    player2.add_card(Card(10, ""))
    player2.add_card(Card(9, ""))

    player3.add_card(Card(10, ""))
    player3.add_card(Card(10, ""))

    player4.add_card(Card(10, ""))

    dialler = Player(("", 0))
    dialler.add_card(Card(10, ""))
    dialler.add_card(Card(9, ""))

    dialler1 = Player(("", 0))
    dialler1.add_card(Card(10, ""))
    dialler1.add_card(Card("Ace", ""))

    assert game_logic.win([player1, player2, player3, player4], dialler)\
           == [(player1, "win"), (player2, "draw"), (player3, "win"), (player4, "lose")]

    assert game_logic.win([player1], dialler1)\
           == [(player1, "draw")]
