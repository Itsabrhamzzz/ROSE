"""
This driver does not do any action.
"""
from rose.common import obstacles, actions  # NOQA

driver_name = "Abraham"


def drive(world):
    x = world.car.x
    y = world.car.y - 1
    your_way = [x//3 * 3, x//3 * 3 + 1, x//3 * 3 + 2]
    obstacle = world.get((x, y))
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
                if world.get((x - 1, y)) not in (obstacles.BARRIER, obstacles.WATER, obstacles.CRACK, obstacles.TRASH,
                                                 obstacles.BIKE):
                    return actions.LEFT
            elif x + 1 in your_way:
                if world.get((x + 1, y)) not in (obstacles.BARRIER, obstacles.WATER, obstacles.CRACK, obstacles.TRASH,
                                                 obstacles.BIKE):
                    return actions.RIGHT
            return prediction(world, x, y, your_way)


def prediction(world, x, y, your_way):
    good_obstacles = (obstacles.PENGUIN, obstacles.CRACK, obstacles.WATER)
    for obstacle in good_obstacles:
        action = check_obstacle(world, x, y, your_way, obstacle)
        if action:
            return action
    return actions.NONE


def check_obstacle(world, x, y, your_way, current_obstacle):
    bad_obstacles = (obstacles.BARRIER, obstacles.TRASH, obstacles.BIKE)
    normal_obstacles = (obstacles.BARRIER, obstacles.WATER, obstacles.CRACK, obstacles.TRASH, obstacles.BIKE)
    if x - 1 in your_way:
        if world.get((x - 1, y)) not in normal_obstacles:
            if current_obstacle == world.get((x - 1, y - 1)):
                return actions.LEFT
            elif current_obstacle == world.get((x - 1, y - 2)) and world.get((x - 1, y - 1)) not in bad_obstacles:
                return actions.LEFT
    if (current_obstacle in (world.get((x, y - 1)), world.get((x, y - 2))) and
            world.get((x, y - 1)) not in bad_obstacles):
        return actions.NONE

    if x + 1 in your_way:
        if world.get((x + 1, y)) not in normal_obstacles:
            if current_obstacle == world.get((x + 1, y - 1)):
                return actions.RIGHT
            elif current_obstacle == world.get((x + 1, y - 2)) and world.get((x + 1, y - 1)) not in bad_obstacles:
                return actions.RIGHT
    return False
