import pytest
from context import src
from src.card import Card
from src.game_logic import GameLogic
from src.player import Player
from src.room import Room

room = Room(GameLogic())


def test_connection():
    room.connect_room(Player(("", 1)))
    room.connect_room(Player(("", 2)))
    room.connect_room(Player(("", 3)))
    dialler = Player(("", 1213))
    room.set_dialler(dialler)

    assert len(room.players) == 3
    assert room.dialler == dialler


def test_current_player():
    room.connect_room(Player(("", 1)))
    assert room.current_player() == Player(("", 1))


def test_next_player():
    player1 = Player(("", 1))
    player2 = Player(("", 2))
    room.connect_room(player1)
    room.connect_room(player2)
    next_player, index = room.next_player()
    assert next_player == player2
    assert index == 1
    assert room.current_player() == player2


def test_win_condition():
    room2 = Room(GameLogic())
    player1 = Player(("", 1))
    player2 = Player(("", 2))
    room2.connect_room(player1)
    room2.set_dialler(player2)
    player1.add_card(Card(10, ""))
    player2.add_card(Card("Ace", ""))
    function_result = room2.win_con()
    expected = [(player1, "lose")]
    assert function_result == expected


def test_start():
    room2 = Room(GameLogic())
    player1 = Player(("", 1))
    player2 = Player(("", 2))
    room2.connect_room(player1)
    room2.set_dialler(player2)
    room2.start()
    assert len(room2.players[0].cards) == 2
    assert len(room2.dialler.cards) == 1
