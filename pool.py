from tile import Tile, Color

class Pool():
    def __init__(self):
        self.all = [Tile(color, value) for color in range(1,4) for value in range(1,13)]
        self.all.append(Tile(0, 0))
        self.all.extend(self.all)