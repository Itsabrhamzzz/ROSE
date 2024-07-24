import random
from rose.common import config, obstacles


class Track(object):
    def __init__(self):
        self._matrix = None
        self.bush_direction_right = 1
        self.bush_direction_left = 1
        self.previous_obstacle = obstacles.NONE
        self.reset()

    # Game state interface

    def update(self):
        """Go to the next game state"""
        self._matrix.pop()
        self._matrix.insert(0, self._generate_row())

    def state(self):
        """Return read only serialize-able state for sending to client"""
        items = []
        for y, row in enumerate(self._matrix):
            for x, obs in enumerate(row):
                if obs != obstacles.NONE:
                    items.append({"name": obs, "x": x, "y": y})
        return items

    # Track interface

    def get(self, x, y):
        """Return the obstacle in position x, y"""
        return self._matrix[y][x]

    def set(self, x, y, obstacle):
        """Set obstacle in position x, y"""
        self._matrix[y][x] = obstacle

    def clear(self, x, y):
        """Clear obstacle in position x, y"""
        self._matrix[y][x] = obstacles.NONE

    def reset(self):
        self._matrix = [
            [obstacles.NONE] * config.matrix_width for x in range(config.matrix_height)
        ]

    def check_bush_on_screen(self):
        places = []
        for row in self._matrix:
            for obstacle in row:
                if obstacle == obstacles.BUSH:
                    places.append([self._matrix.index(row), row.index(obstacles.BUSH)])
        if places:
            return places
        return False
    # Private

    def _generate_row(self):
        """
        Generates new row with obstacles

        Try to create fair but random obstacle stream. Each player get the same
        obstacles, but in different cells if 'is_track_random' is True.
        Otherwise, the tracks will be identical.
        """
        row = [obstacles.NONE] * config.matrix_width
        obstacle = obstacles.get_random_obstacle()
        bush_place = self.check_bush_on_screen()
        if bush_place:
            if bush_place[0][0]//3 * 3 <= bush_place[0][0] + self.bush_direction_left <= bush_place[0][0]//3 * 3 + 2:
                self.previous_obstacle = self._matrix[bush_place[0][0] + self.bush_direction_left][bush_place[0][1]]
                self._matrix[bush_place[0][0] + self.bush_direction_left][bush_place[0][1]]\
                    = self._matrix[bush_place[0][0]][bush_place[0][1]]
                self._matrix[bush_place[0][0]][bush_place[0][1]] = self.previous_obstacle
            else:
                self.bush_direction_left *= -1
            while obstacle == obstacles.BUSH:
                obstacle = obstacles.get_random_obstacle()
        if config.is_track_random:
            for lane in range(config.max_players):
                low = lane * config.cells_per_player
                high = low + config.cells_per_player
                cell = random.choice(range(low, high))
                row[cell] = obstacle
        else:
            cell = random.choice(range(0, config.cells_per_player))
            for lane in range(config.max_players):
                row[cell + lane * config.cells_per_player] = obstacle
        return row
