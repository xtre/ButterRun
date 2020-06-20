import socket  # Import socket module
from threading import Thread

s = 0
player_y = 0


def init():
    global s
    s = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = 12345  # Reserve a port for your service.

    s.connect((host, port))

    thread1 = Thread(target=connection)
    thread1.start()


def send_position(py):
    s.send(str(py).encode('UTF-8'))


def connection():
    global player_y
    try:
        while True:
            data = s.recv(32)
            #print(data)
            player_y = data
            if not data:
                break
    except Exception as ex:
        print(ex)

