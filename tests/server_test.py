import pytest
from context import src
from src.player import Player
from src.server import Server


def test_create_room():
    server = Server()
    server.create_room()
    assert len(server.rooms) == 1


def test_start_room():
    player = Player(("", 0))
    server = Server()
    server.create_room()
    server.connect_room_as_player(player, 1)
    server.connect_room_as_dialer(Player(("", 0)), 1)
    server.start_game(1)
    assert len(server.rooms[1].current_player().cards) == 2
    assert len(server.rooms[1].dialler.cards) == 1


def test_display_rooms():
    server = Server()
    server.create_room()
    function_result = server.display_rooms()
    expected = f"\nRoom #1\n"
    assert function_result == expected


def test_player_connection():
    player = Player(("", 0))
    server = Server()
    server.create_room()
    assert server.connect_room_as_player(player, 1)
    assert not server.connect_room_as_player(player, 2)


def test_dialler_connection():
    dialler = Player(("", 0))
    server = Server()
    server.create_room()
    assert server.connect_room_as_dialer(dialler, 1)
    assert not server.connect_room_as_dialer(dialler, 2)


def test_take_card():
    player = Player(("", 0))
    server = Server()
    server.create_room()
    server.connect_room_as_player(player, 1)
    server.connect_room_as_dialer(Player(("", 0)), 1)
    server.start_game(1)
    server.take_card(1)
    assert len(server.rooms[1].current_player().cards) == 3
