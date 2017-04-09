from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    @staticmethod
    def get_opposite_direction(direction):
        if direction == Direction.UP:
            return Direction.DOWN
        if direction == Direction.DOWN:
            return Direction.UP
        if direction == Direction.LEFT:
            return Direction.RIGHT
        if direction == Direction.RIGHT:
            return Direction.LEFT


