from classes.tile import Tile
from classes.color import Color

class Pool():
    def __init__(self, tiles=None):
        self.tiles = tiles
        if self.tiles is None:
            self.tiles = [Tile(color, value) for color in range(1,5) for value in range(1,14) for _ in range(2)] + [Tile(0,0), Tile(0,0)]

    def add_tiles(self, tiles):
        if type(tiles) is Tile:
            self.tiles.append(tiles)
        elif type(tiles) is list:
            self.tiles.extend(tiles)

    def active_tiles(self):
        return [tile for tile in self.tiles if tile.visible == True]
    
    def inactive_tiles(self):
        return [tile for tile in self.tiles if tile.visible == False]

    def available_tiles(self):
        return [tile for tile in self.tiles if tile.available == True]

    def unavailable_tiles(self):
        return [tile for tile in self.tiles if tile.available == False]

    def get_values(self):
        return [tile.value for tile in self.tiles]

    def get_colors(self):
        return [tile.color for tile in self.tiles]
    
    def sum(self):
        return sum(self.get_values())

    def color_sort(self):
        colors = {
            'BLACK': [],
            'BLUE': [],
            'ORANGE': [],
            'RED': [],
            'JOKER': []
        }
        for tile in self.tiles:
            colors[tile.color.name].append(tile)

        return colors

    def value_sort(self):
        values = [[] for _ in range(14)]
        for tile in self.tiles:
            values[tile.value].append(tile)

        return values

    def get_groups(self):
        values = self.value_sort()
        groups = [set(values[i]) for i in range(1, len(values)) if len(values[i]) > 0]

        return groups

    def get_clusters(self, values):
        clusters = []
        cluster = []
        i = 1
        while i < 14:
            if len(values[i]) != 0:
                cluster.append(i)
            else:
                clusters.append(cluster.copy())
                cluster = []
            i += 1
        return [x for x in clusters if len(x) != 0]

    def get_runs(self):
        values = self.value_sort()
        number_clusters = self.get_clusters(values)

        # runs = [[]]
        # for cluster in number_clusters:
        #     tile_cluster = [[]]
        #     for num in cluster:
        #         for _ in values[num]:
        #             for t in tile_cluster:
        #                 tile_cluster.append(t.copy().append())
        #                 tile_cluster.remove(t)

        # number_clusters = [[1,2,3], [5]]
        # values = [{BLUE_1, ORANGE_1}, {RED_2}, {BLUE_3, BLACK_3, RED_3}, {RED_5}]
        """
        runs = [
            [BLUE_1, RED_2, BLUE_3],
            [ORANGE_1, RED_2, BLUE_3],
            [BLUE_1, RED_2, BLACK_3],
            [ORANGE_1, RED_2, BLACK_3],
            [BLUE_1, RED_2, RED_3],
            [ORANGE_1, RED_2, RED_3], 
            [RED_5]
        ]
        """
        runs = []
        for number_cluster in number_clusters:
            # [1,2,3]
            this_run = [[]]
            for number in number_cluster:
                # 1
                for i in range(len(values[number])):
                    # 2 ({BLUE_1, ORANGE_1})
                    to_be_deleted = []
                    for array in this_run:
                        # []
                        print(f'array:{array}')
                        print(f'i:{i}')
                        print(f'number:{number}')
                        print(f'tile:{values[number][i]}\n\n')
                        # tile = values[number][i]
                        # this_run.append(array.copy().append(tile))
                        # print(f'appended:{array.append(tile)}')
                        # to_be_deleted = array
                    # this_run.remove(to_be_deleted)
            runs.append(this_run)


        '''
        # 1. get adjacent number groups (e.g., [[1,2],[4,5,6], ...])
        2. build runs array
            a. start with empty array
            b. if number has multiple tiles, duplicate the original array(s) that many times
            c. append first tile to first fraction, second to second fraction, etc.
        '''

        return runs

    def get_sets(self):
        pass

