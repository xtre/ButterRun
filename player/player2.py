from src.images import images

img = 0

player2_y = 300
score = 0


def init(pg):
    global img
    img = pg.image.load(images.player_image)