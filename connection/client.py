import logging
import socket  # Import socket module
from random import randrange
from threading import Thread
from src.utilities import timer

running = True
ai_mode = False
s = 0
player2_y = 0
ball_x = 400
ball_y = 300
score1 = 0
score2 = 0
respawn_time = 0


def init(address):
    global s
    global ai_mode

    if address == "":
        ai_mode = True
        return

    address = address.split(":")
    s = socket.socket()  # Create a socket object
    host = address[0]
    port = address[1]

    s.connect((host, int(port)))

    thread1 = Thread(target=connection)
    thread1.start()


def send(player):
    s.send((str(player.player_y) + ";" + str(player.player_m) + ":").encode('UTF-8'))


def connection():
    global player2_y
    global ball_x
    global ball_y
    global score1
    global score2
    global respawn_time
    try:
        while running:
            data = s.recv(1024)
            if not data:
                print("Received no data")
                break

            latest = str(data.decode("utf-8")).split(":")[-2]
            py_bx_by = latest.split(";")

            player2_y = int(str(py_bx_by[0]))
            ball_x = -(int(py_bx_by[1]) - (800 - (46 - 6)))
            ball_y = int(py_bx_by[2])
            score1 = int(py_bx_by[3])
            score2 = int(py_bx_by[4])
            respawn_time = int(py_bx_by[5])
    except Exception as ex:
        logging.exception(ex)


def stop():
    global running
    running = False


ball_xm = -1
ball_ym = 0
ball_outofbounds = False
ball_respawning = False
timer_start = False
timer.ending = 5
player2_m = 0


def update_ai(player1, player2):
    global ball_x
    global ball_y
    global ball_xm, ball_ym
    global ball_outofbounds
    global ball_respawning
    global player2_y
    global timer_start
    global respawn_time
    global player2_m

    if player1.player_y < ball_y:
        player2_m = 1
    else:
        player2_m = -1

    player2_y = player2_y + player2_m

    timer.update()
    respawn_time = 3 - timer.time
    if ball_outofbounds:
        ball_outofbounds = False
        timer_start = True
        timer.reset(True)
    if timer_start:
        if respawn_time < 0:
            timer_start = False
            ball_respawning = False
            ball_xm = -ball_xm
    else:
        timer.time = 0

    if not ball_respawning:
        ball_x = ball_x + ball_xm
        ball_y = ball_y + ball_ym/2

    if ball_x < 32:
        if ball_y + 46 > player2.player_y and ball_y < player2.player_y + 128:
            ball_xm = -ball_xm
            ball_ym = (player2.player_m/2) + ((1 + randrange(25)) - 15) * 0.01

    if ball_x > (800 - (32 + 46)):
        if ball_y + 46 > player1.player_y and ball_y < player1.player_y + 128:
            ball_xm = -ball_xm
            ball_ym = (player2_m/2) + ((1 + randrange(25)) - 15) * 0.01

    if ball_x < 0:
        player1.score = player1.score + 1
        ball_x = 400 - 23
        ball_y = 300 - 23
        ball_outofbounds = True
        ball_respawning = True
    elif ball_x > 800:
        player2.score = player2.score + 1
        ball_x = 400 - 23
        ball_y = 300 - 23
        ball_outofbounds = True
        ball_respawning = True

    if ball_y < 0:
        ball_ym = -ball_ym
    elif ball_y > 600 - 46:
        ball_ym = -ball_ym
