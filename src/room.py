from typing import Union
from src.game_logic import GameLogic
from src.player import Player
from src.deck import Deck


class Room:
    def __init__(self, game_logic: GameLogic) -> None:
        self.__game_logic: GameLogic = game_logic
        self.__players: list[Player] = []
        self.ready_to_play: int = 0
        self.__dialler: Player = None
        self.__deck: Deck = Deck()
        self.__deck.init_deck()
        self.__room_status: str = "Not started"
        self.__index: int = 0

    def start(self) -> None:
        self.__room_status = "Started"
        for player in self.__players:
            player.take_card(self.__deck)
            player.take_card(self.__deck)

        self.__dialler.take_card(self.__deck)

    def connect_room(self, player: Player) -> None:
        self.__players.append(player)

    def set_dialler(self, dialler: Player) -> None:
        self.__dialler = dialler

    def current_player(self) -> Union[Player, None]:
        if self.__index >= len(self.__players):
            return None
        return self.__players[self.__index]

    def next_player(self) -> tuple[Union[Player, None], int]:
        self.__index += 1
        if self.__index >= len(self.__players):
            return None, self.__index

        return self.__players[self.__index], self.__index

    def win_con(self) -> list[tuple[Player, str]]:
        wins = self.__game_logic.win(self.__players, self.__dialler)
        # for player in wins:
        #     print(player)
        return wins

    @property
    def deck(self) -> Deck:
        return self.__deck

    @property
    def dialler(self) -> Union[Player, None]:
        return self.__dialler

    @property
    def players(self) -> list[Player]:
        return self.__players

    @property
    def status(self) -> str:
        return self.__room_status

    @status.setter
    def status(self, status: str) -> None:
        self.__room_status = status
