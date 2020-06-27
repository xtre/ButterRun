from datetime import datetime

tick = 0
time = 0

ending = 0


def update():
    global tick
    global time

    x = datetime.today()
    y = x.replace(day=x.day, hour=0, minute=0, second=0, microsecond=0)
    delta_t = y - x

    if tick != delta_t.seconds:
        tick = delta_t.seconds
        time = time + 1

    return time


def ending():
    return time >= ending


def reset(to_start):
    global time
    if to_start:
        time = 0
    else:
        time = ending

