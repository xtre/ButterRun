import pygame

from src.images import images

move_left = pygame.K_a
move_right = pygame.K_d

img = 0

player_y = 300
player_m = 0
score = 0


def init(pg):
    global img
    img = pg.image.load(images.player_image)


def update_movement(keys):
    global player_y
    global player_m

    player_m = 0
    if keys[pygame.K_w] and player_y > 0:
        player_m = -1
    if keys[pygame.K_s] and player_y < 600-128:
        player_m = 1

    player_y = player_y + player_m
