from rose.common import obstacles, actions  # NOQA

driver_name = "Smart Abraham"
scores = (10, 15, -10, 20, -10, 14, -10)
action = (0, 1, -1)


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
            return actions.ALL[prediction(world, x, y, your_way, 0)[1]]
        case _:
            if x - 1 in your_way:
                return actions.LEFT
            return actions.RIGHT


# def prediction(world, x, y, your_way, best_score):
#     current_score = 0
#     best_action = 0
#     if y >= 0:
#         best_score += scores[obstacles.ALL.index(world.get((x, y)))]
#         for i in range(len(action)):
#             if x + action[i] in your_way:
#                 new_score, act = prediction(world, x + action[i], y - 1, your_way, best_score)
#                 if new_score > current_score:
#                     current_score = new_score
#                     best_action = i
#     if current_score > best_score:
#         best_score = current_score
#     return best_score, best_action


def prediction(world, x, y, your_way, score):
    best_action = 0
    if y >= 0 and x in your_way:
        score += scores[obstacles.ALL.index(world.get((x, y)))]
        new_score1, act1 = prediction(world, x + action[0], y - 1, your_way, score)
        new_score2, act2 = prediction(world, x + action[1], y - 1, your_way, score)
        new_score3, act3 = prediction(world, x + action[2], y - 1, your_way, score)
        new_scores = [new_score1, new_score2, new_score3]
        score = max(new_scores)
        best_action = new_scores.index(score)
    return score, best_action

