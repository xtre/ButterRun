import pygame
import time
from src.main.player import player

pg = pygame
pg.init()

screen = pg.display.set_mode((800, 600))

# Frames Per Seconds variable
fps = 0
# Text font entity from Pygame
font = pg.font.Font(None, 30)

# Player image
img = player.get_image(pg)

# Game Loop
running = True
while running:
    # Clears all from the screen
    screen.fill((0, 128, 0))

    # Prepare text to be rendered
    f = font.render(str(round(((time.time() * 1000) - fps))), True, pg.Color('white'))
    # Render the text at this line. Anything after will be shown as over it and anything before will be under it
    screen.blit(f, (50, 50))
    fps = int(round(time.time() * 1000))

    # Render image now
    screen.blit(img, (10, 10))

    # What the close button does
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # updates the screen with what has been done before this line
    pg.display.update()