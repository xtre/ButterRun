import socket  # Import socket module
from threading import Thread

running = True
s = 0
player2_y = 0


def init(address):
    global s
    address = address.split(":")
    s = socket.socket()  # Create a socket object
    host = address[0]
    port = address[1]

    s.connect((host, int(port)))

    thread1 = Thread(target=connection)
    thread1.start()


def send_position(py):
    s.send((str(py)+":").encode('UTF-8'))


def connection():
    global player2_y
    try:
        while running:
            data = s.recv(1024)
            if not data:
                print("Received no data")
                break
            player2_y = int(str(data.decode("utf-8")).split(":")[-2])
            # data = s.recv(32)
            # print(data)
            # player_y = data
            # if not data:
            #     break
    except Exception as ex:
        print(ex)


def stop():
    global running
    running = False