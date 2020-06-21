import pygame
import time
from src.main.player import player
from src.main.player import player2
from src.main.connection import client

client.init(input("Ask user for something."))

pg = pygame
pg.init()

player.init(pg)
player2.init(pg)

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
    client.send_position(player.player_y)

    # Clears all from the screen
    screen.fill((0, 128, 0))

    # Prepare text to be rendered
    f = font.render(str(round(((time.time() * 1000) - fps))), True, pg.Color('white'))
    # Render the text at this line. Anything after will be shown as over it and anything before will be under it
    screen.blit(f, (50, 50))
    fps = int(round(time.time() * 1000))

    # Render image now
    screen.blit(player.img, (10, player.player_y))
    screen.blit(player2.img, (800 - 32, int(player2.player_y)))

    # What the close button does
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            client.stop()

    # updates the screen with what has been done before this line
    pg.display.update()
