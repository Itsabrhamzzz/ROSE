* `obstacles.BUSH`   you must return `actions.RIGHT` or `actions.LEFT` to bypass
                        the obstacle. Any other action will cause you to
                        stay in place.
                        Score: 0 for `LEFT`/`RIGHT` otherwise -30


The bush appears once to the two of the car lane:


    <------ Car#1 lane ------><------ Car#2 lane ---->

    |       |       |       |X|       |       |      |
    |       |       |       |X|       |       |      |
    |       |       |       |X|       |       |      |
    |       |       |       |X|       |       |      |
    |  BUSH |       |       |X|       |       | BUSH |
    |       |       |       |X|       |       |      |
    |       |       |       |X|       |       |      |
    |       |       |       |X|       |       |      |
    |       |       |       |X|       |       |      |
    |       | car#1 |       |X|       | Car#2 |      |
    |       |       |       |X|       |       |      |
    |       |       |       |X|       |       |      |

It moves diagonally, it bounces against the border of the two car lanes and external borders:

    <------ Car#1 lane ------><------ Car#2 lane ---->

    |       |       |       |X|       |       |      |
    |       |       |       |X|       |       |      |
    |       |       |       |X|       |       |      |
    |       |       |       |X|       |       |      |
    |       |       |       |X|       |       | BUSH |
    |       |       |       |X|       |   ↙   |      |
    |       |       |  BUSH |X| BUSH  |       |      |
    |       |   ↙   |       |X|       |   ↘   |      |
    |       |       |       |X|       |       |      |
    |       | car#1 |       |X|       | Car#2 |      |
    |       |       |       |X|       |       |      |
    |       |       |       |X|       |       |      |


* `obstacles.BIRD`   return `actions.PICKUP` and move forward. You will
                        move forward even if you do not pick up the penguin.
                        Score : 30 for `PICKUP` otherwise 0

The bird moves horizontally from one car border to the other border from the other car

    <------ Car#1 lane ------><------ Car#2 lane ---->

    |       |       |       |X|       |       |       |
    |       |       |       |X|       |       |       |
    |       |       |       |X|       |       |       |
    |       |       |       |X|       |       |       |
    |       |       |       |X|       |       |       |
    |   ←   | BIRD1 |       |X|       |   ←   | BIRD1 |
    |       |       |       |X|       |       |       |
    |       |       |       |X|       |       |       |
    |       |       |       |X|       |       |       |
    |       | car#1 |       |X|       | Car#2 |       |
    |       |       |       |X|       |       |       |
    |       |       |       |X|       |       |       |