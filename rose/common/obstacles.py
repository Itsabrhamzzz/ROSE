""" Game obstacles """

import random

NONE = ""  # NOQA
CRACK = "crack"  # NOQA
TRASH = "trash"  # NOQA
PENGUIN = "penguin"  # NOQA
BIKE = "bike"  # NOQA
WATER = "water"  # NOQA
BARRIER = "barrier"  # NOQA
BUSH = "bush"  # NOQA
BIRD = "bird"
ALL = (NONE, CRACK, TRASH, PENGUIN, BIKE, WATER, BARRIER, BUSH, BIRD)


def get_random_obstacle():
    return random.choice(ALL)
