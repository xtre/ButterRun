from src.images import images

img = 0

ball_x = 0
ball_y = 100


def init(pg):
    global img
    img = pg.image.load(images.ball_image)