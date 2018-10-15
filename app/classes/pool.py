from classes.tile import Tile, Color

class Pool():
    def __init__(self, tiles=None):
        self.tiles = tiles
        if self.tiles is None:
            self.tiles = [Tile(color, value) for color in range(1,5) for value in range(1,14) for _ in range(2)] + [Tile(0,0), Tile(0,0)]

    def active_tiles(self):
        return [tile for tile in self.tiles if tile.visible == True]
    
    def inactive_tiles(self):
        return [tile for tile in self.tiles if tile.visible == False]

    def available_tiles(self):
        return [tile for tile in self.tiles if tile.available == True]

    def unavailable_tiles(self):
        return [tile for tile in self.tiles if tile.available == False]

    def get_groups(self, tiles):
        sets = [[] for _ in range(14)]
        values = [[] for _ in range(14)]
        
        for tile in tiles:
            values[tile.value].append(tile)

        for i in range(len(values)):
            found = {
                'BLACK': False,
                'BLUE': False,
                'ORANGE': False,
                'RED': False,
                'NONE': False
            }

            for tile in values[i]:
                if not found[tile.color.name]:
                    sets[i].append(tile)
                    found[tile.color.name] = True
        
        groups = [set for set in sets if len(set) >= 3]
        # print("groups: {}".format(groups))
        return groups

