import socket
import threading
import time


working = True
ur_turn = False
game_start = False


def receving(sock):
    global ur_turn, game_start
    while working:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(str(data.decode('utf-8')))
                time.sleep(0.2)
                dedata = data.decode('utf-8')
                if dedata == "200 your_turn":
                    ur_turn = True
                elif dedata == "200 start_game":
                    game_start = True
                elif "200 result" in dedata:
                    res = str(data.decode('utf-8')).split(" ")
                    print(f"result: {res[2]}")

        except Exception as e:
            pass


host = socket.gethostbyname(socket.gethostname())
port = 0

server = (socket.gethostbyname(socket.gethostname()), 22)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(False)

recv_thread = threading.Thread(target=receving, args=(s,))
recv_thread.start()
room_number = 0
role = ""

while working:
    try:
        message = input("Enter a message > ")
        if message == "create":
            s.sendto("create room".encode("utf8"), server)
        elif message == "display rooms":
            s.sendto("display rooms".encode("utf8"), server)

        elif message == "join player":
            room_number = int(input("Enter a room number > "))
            role = "player"
            s.sendto(f"join player {room_number}".encode("utf8"), server)

        elif message == "join dialler":
            room_number = int(input("Enter a room number > "))
            role = "dialler"
            s.sendto(f"join dialler {room_number}".encode("utf8"), server)

        elif message == "start":
            s.sendto(f"start {room_number}".encode("utf8"), server)
            break

    except KeyboardInterrupt as e:
        working = False


print("Waiting for ur turn...")
while working:
    try:
        if ur_turn:
            message = input("Action > ")
            if message == "take card":
                s.sendto(f"{role} take_card {room_number}".encode("utf8"), server)
            elif message == "skip":
                s.sendto(f"{role} skip {room_number}".encode("utf8"), server)
                ur_turn = False
                break

    except KeyboardInterrupt as e:
        working = False
print("Wait for the end...")

while working:
    try:
        pass
    except KeyboardInterrupt as e:
        working = False

recv_thread.join()
s.close()
