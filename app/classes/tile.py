from enum import Enum
import uuid

class Color(Enum):
    JOKER = 0
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
        return '{}_{}'.format(self.color.name, self.value)

    def __hash__(self):
        if self.color == Color.JOKER:
            return hash((self.color, self.value, uuid.uuid4()))
        return hash((self.color, self.value))
        
    def __eq__(self, other):
        return self.color == other.color and self.value == other.value

    def __lt__(self, other):
        return self.value < other.value
    
    def equals_color(self, other):
        return self.color == other.color

    def equals_value(self, other):
        return self.value == other.value
