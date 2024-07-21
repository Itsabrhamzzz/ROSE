from rose.common import obstacles, actions

driver_name = "Michael Schumacher"


def find_path(world, start):
    queue = [start]
    came_from = {start: None}

    while queue:
        current = queue.pop(0)

        x, y = current
        neighbors = [(x, y - 1), (x - 1, y), (x + 1, y)]

        for next_pos in neighbors:
            try:
                obstacle = world.get(next_pos)
            except IndexError:
                continue

            if next_pos not in came_from:
                if obstacle not in (obstacles.BARRIER, obstacles.TRASH, obstacles.BIKE):
                    queue.append(next_pos)
                    came_from[next_pos] = current

    path = []
    goal = (start[0], 0)
    current = goal
    while current and current in came_from:
        path.append(current)
        current = came_from[current]

    path.reverse()
    return path


def handle_obstacle(obstacle):
    if obstacle == obstacles.NONE:
        return actions.NONE
    elif obstacle == obstacles.PENGUIN:
        return actions.PICKUP
    elif obstacle == obstacles.WATER:
        return actions.BRAKE
    elif obstacle == obstacles.CRACK:
        return actions.JUMP
    elif obstacle in (obstacles.TRASH, obstacles.BIKE, obstacles.BARRIER):
        return actions.RIGHT  # Or actions.LEFT
    else:
        return actions.NONE


def drive(world):
    x = world.car.x
    y = world.car.y

    start = (x, y)
    path = find_path(world, start)

    if len(path) > 1:
        next_step = path[1]
        try:
            obstacle = world.get(next_step)
        except IndexError:
            obstacle = None
        return handle_obstacle(obstacle)
    else:
        return actions.NONE
