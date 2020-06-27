from threading import Thread

import pygame
import time

from src.ball import ball
from src.player import player
from src.player import player2
from src.connection import client

client.init(input("Enter Address or press enter for AI"))

pg = pygame
pg.init()

player.init(pg)
player2.init(pg)
ball.init(pg)

screen = pg.display.set_mode((800, 600))

# Frames Per Seconds variable
fps = 0
# Text font entity from Pygame
font = pg.font.Font(None, 30)

# Game Loop
running = True
while running:
    player.update_movement(pygame.key.get_pressed())
    player2.player_y = client.player2_y

    if client.ai_mode:
        client.update_ai(player2, player)
    else:
        client.send(player)

    ball.ball_x = client.ball_x
    ball.ball_y = client.ball_y
    player.score = client.score1
    player2.score = client.score2

    # Clears all from the screen
    screen.fill((0, 64, 64))

    # Prepare text to be rendered
    f = font.render(str(player.score) + " : " + str(player2.score), True, pg.Color('white'))
    # Render the text at this line. Anything after will be shown as over it and anything before will be under it
    screen.blit(f, (50, 50))
    fps = int(round(time.time() * 1000))

    # Render image now
    screen.blit(player.img, (0, player.player_y))
    screen.blit(player2.img, (800 - 32, int(player2.player_y)))
    screen.blit(ball.img, (int(ball.ball_x), int(ball.ball_y)))
    if client.respawn_time > 0:
        screen.blit(font.render(str(client.respawn_time), True, pg.Color('white')), (50, 74))

    # What the close button does
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            client.stop()

    # updates the screen with what has been done before this line
    pg.display.update()
