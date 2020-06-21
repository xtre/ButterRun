import pygame

move_left = pygame.K_a
move_right = pygame.K_d

img = 0

player_y = 300


def init(test):
    global img
    img = test.image.load('Paddle.png')


def update_movement(keys):
    global player_y
    if keys[pygame.K_w] and player_y > 0:
        player_y = player_y - 1
    if keys[pygame.K_s] and player_y < 600-128:
        player_y = player_y + 1
