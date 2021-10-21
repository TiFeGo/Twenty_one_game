import socket

from src.player import Player
from src.room import Room
from src.game_logic import GameLogic


class Server:

    def __init__(self):
        self.__host = socket.gethostbyname(socket.gethostname())
        self.__port = 22
        self.__clients = []
        self.__sock = None

        self.__rooms: dict[int, Room] = {}
        self.__response = ""

        self.__game_logic = GameLogic()

    def __init_socket(self):
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__sock.bind((self.__host, self.__port))

    def run(self):
        self.__init_socket()
        working = True

        while working:
            try:
                data, addr = self.__sock.recvfrom(1024)

                print(f"addr {addr}")

                if addr not in self.__clients:
                    self.__clients.append(addr)

                self.request_handler(data, addr)

            except KeyboardInterrupt as e:
                print("Stop working")
                working = False

    def __del__(self):
        if self.__sock:
            print("Closed")
            self.__sock.close()

    def request_handler(self, request: bytes, addr: tuple[str, int]):
        request = request.decode('utf-8')
        if request != "" or request is not None:
            parts = request.split(' ')
            action = parts[0]
            if action == "create":
                self.create_room()
                self.send_response(addr, "created successfully", 200)

            elif action == "display":
                self.display_action(parts, addr)

            elif action == "join":
                self.join_action(parts, addr)

            elif action == "start":
                self.start_action(parts)

            elif action == "player":
                self.player_action(parts)

            elif action == "dialler":
                self.dialler_action(parts)

    def create_room(self):
        n = len(self.__rooms) + 1
        room = Room(self.__game_logic)
        self.__rooms[n] = room

    def display_action(self, parts: list[str], addr: tuple[str, int]) -> None:
        obj = parts[1]
        if obj == "rooms":
            response_body = self.display_rooms()
            self.send_response(addr, response_body, 200)
        elif obj == "free_places":
            room_number = int(parts[2])
            self.display_rooms_free_places(room_number)

    def join_action(self, parts: list[str], addr: tuple[str, int]) -> None:
        obj = parts[1]
        room_number = int(parts[2])

        if obj == "player":
            joined = self.connect_room_as_player(Player(addr), room_number)
            body = f"Connected room {room_number} as a player" if joined \
                else f"Not connected room {room_number} as a player"

            self.send_response(addr, body, 200)

        elif obj == "dialler":
            joined = self.connect_room_as_dialer(Player(addr), room_number)
            body = f"Connected room {room_number} as a dialler" if joined \
                else f"Not connected room {room_number} as a dialler"

            self.send_response(addr, body, 200)

    def start_action(self, parts: list[str]) -> None:
        room_number = int(parts[1])
        self.__rooms[room_number].ready_to_play += 1
        if len(self.__rooms[room_number].players) + 1 == self.__rooms[room_number].ready_to_play and \
                self.__rooms[room_number].dialler is not None:
            self.start_game(room_number)
            self.__rooms[room_number].status = "started"
            for player in self.__rooms[room_number].players:
                self.send_response(player.address, f"start_game", 200)
                self.send_response(player.address, f"{player.display_card()}", 200)
                self.send_response(player.address, f"{self.__rooms[room_number].dialler.display_card()}", 200)

            self.send_response(self.__rooms[room_number].players[0].address, f"your_turn", 200)

    def player_action(self, parts: list[str]) -> None:
        game_action = parts[1]
        room_number = int(parts[2])
        if game_action == "take_card":
            self.__rooms[room_number].current_player().take_card(self.__rooms[room_number].deck)
            self.send_response(self.__rooms[room_number].current_player().address,
                               f"{self.__rooms[room_number].current_player().display_card()}", 200)

        elif game_action == "skip":
            self.__rooms[room_number].next_player()
            if self.__rooms[room_number].current_player() is not None:
                self.send_response(self.__rooms[room_number].current_player().address, f"your_turn", 200)
            else:
                self.send_response(self.__rooms[room_number].dialler.address, f"your_turn", 200)
                self.send_response(self.__rooms[room_number].dialler.address,
                                   f"ur card {self.__rooms[room_number].dialler.display_card()}", 200)

    def dialler_action(self, parts: list[str]) -> None:
        game_action = parts[1]
        room_number = int(parts[2])
        if game_action == "take_card":
            self.__rooms[room_number].dialler.take_card(self.__rooms[room_number].deck)
            self.send_response(self.__rooms[room_number].dialler.address,
                               f"{self.__rooms[room_number].dialler.display_card()}", 200)
        elif game_action == "skip":
            game_results = self.__rooms[room_number].win_con()
            for player, result in game_results:
                self.send_response(player.address, f"u {result}", 200)

    def display_rooms(self) -> str:
        response_body = ""
        for room_number in self.__rooms.keys():
            if self.__rooms[room_number].status == "Not started":
                response_body += f"\nRoom #{room_number}\n"
        return response_body

    def display_rooms_free_places(self, room_number: int):
        pass

    def connect_room_as_player(self, player: Player, room_number: int) -> bool:
        if room_number in self.__rooms.keys():
            self.__rooms[room_number].connect_room(player)
            return True
        return False

    def connect_room_as_dialer(self, player: Player, room_number: int) -> bool:
        if room_number in self.__rooms.keys() and self.__rooms[room_number].dialler is None:
            self.__rooms[room_number].set_dialler(player)
            return True
        return False

    def start_game(self, room_number: int):
        self.__rooms[room_number].start()

    def take_card(self, room_number: int):
        if self.__rooms[room_number].current_player():
            self.__rooms[room_number].current_player().take_card(self.__rooms[room_number].deck)

    def skip_turn(self):
        pass

    def send_response(self, addr: tuple[str, int], body: str, code: int):
        if code == 200:
            self.__sock.sendto(f"200 {body}".encode("utf-8"), addr)

    # send_response to players
    def end_game(self):
        pass

    @property
    def rooms(self) -> dict[int, Room]:
        return self.__rooms


if __name__ == '__main__':
    server = Server()
    server.run()
