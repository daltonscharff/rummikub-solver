from enum import Enum

class Color(Enum):
    NONE = 0
    BLACK = 1
    BLUE = 2
    ORANGE = 3
    RED = 4

class Tile():
    def __init__(self, color, value, visible=False):
        self.color = Color(color)
        self.value = value
        self.visible = visible

    def __repr__(self):
        return "{}:{}".format(self.color.name, self.value)
