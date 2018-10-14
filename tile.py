from enum import Enum
import uuid

class Color(Enum):
    NONE = 0
    BLACK = 1
    BLUE = 2
    ORANGE = 3
    RED = 4

class Tile():
    def __init__(self, color, value, available=True, in_play=False):
        self.color = Color(color)
        self.value = value
        self.available = available
        self.in_play = in_play

    def __repr__(self):
        return "{}:{}".format(self.color.name, self.value)
