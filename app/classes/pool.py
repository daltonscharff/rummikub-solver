from classes.tile import Tile, Color

class Pool():
    def __init__(self):
        self.tiles = [Tile(color, value) for color in range(1,5) for value in range(1,14) for _ in range (0,2)]
        self.tiles.extend([Tile(0, 0), Tile(0, 0)])

    def active_tiles(self):
        return [tile for tile in self.tiles if tile.visible == True]
    
    def inactive_tiles(self):
        return [tile for tile in self.tiles if tile.visible == False]

    def available_tiles(self):
        return [tile for tile in self.tiles if tile.available == True]

    def unavailable_tiles(self):
        return [tile for tile in self.tiles if tile.available == False]
