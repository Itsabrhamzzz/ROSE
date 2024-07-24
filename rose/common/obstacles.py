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
ALL = (NONE, CRACK, TRASH, PENGUIN, BIKE, WATER, BARRIER, BUSH)


def get_random_obstacle():
    return random.choice(ALL)
