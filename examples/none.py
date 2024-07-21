"""
This driver does not do any action.
"""
from rose.common import obstacles, actions  # NOQA

driver_name = "Avraham"


def drive(world):
    x = world.car.x
    y = world.car.y
    your_way = [x//3 * 3, x//3 * 3 + 1, x//3 * 3 + 2]
    obstacle = world.get((x, y - 1))
    match obstacle:
        case obstacles.PENGUIN:
            return actions.PICKUP
        case obstacles.CRACK:
            return actions.JUMP
        case obstacles.WATER:
            return actions.BRAKE
        case obstacles.NONE:
            return prediction(world, x, y, your_way)
        case _:
            if x - 1 in your_way:
                return actions.LEFT
            return actions.RIGHT


def prediction(world, x, y, your_way):
    if obstacles.PENGUIN in (world.get((x - 1, y - 2)), world.get((x - 1, y - 2))) and x - 1 in your_way:
        return actions.LEFT
    elif obstacles.PENGUIN in (world.get((x, y - 2)), world.get((x, y - 2))):
        return actions.NONE
    elif obstacles.PENGUIN in (world.get((x + 1, y - 2)), world.get((x + 1, y - 2))) and x + 1 in your_way:
        return actions.RIGHT
    else:
        return actions.NONE
