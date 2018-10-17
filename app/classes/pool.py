from classes.tile import Tile, Color

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
            'NONE': []
        }
        for tile in self.tiles:
            colors[tile.color.name].append(tile)

        return colors

    def value_sort(self):
        values = [[] for _ in range(14)]
        for tile in self.tiles:
            values[tile.value].append(tile)

        return values

    def place_jokers_in_groups(self, sets, values):
        if len(self.tiles) == len(values[0]):
            raise ValueError('Jokers cannot be placed without other groups')

        joker_stack = values[0].copy()
        groups_ge_3 = [s for s in sets if len(s) >= 3]
        groups_eq_2 = [s for s in sets if len(s) == 2]
        groups_eq_1 = [s for s in sets if len(s) == 1]
        
        while len(joker_stack) > 0:
            groups_of_1_and_2 = groups_eq_2 + groups_eq_1
            max_set_index = -1
            for i in range(len(groups_of_1_and_2)):     
                # Implementing a way to get rid of the most cards would be a more win-centric strategy
                max_set_index = -1
                max_sum = -1
                current_sum = sum([tile.value for tile in groups_of_1_and_2[i]])
                if current_sum > max_sum:
                    max_sum = current_sum
                    max_set_index = i
            if max_set_index != -1:
                while len(groups_of_1_and_2[max_set_index]) < 3 and len(joker_stack) > 0:
                    groups_of_1_and_2[max_set_index].update([joker_stack.pop()])
                if len(groups_of_1_and_2[max_set_index]) >= 3:
                    groups_ge_3.append(groups_of_1_and_2.pop(max_set_index))
            else:
                while len(joker_stack) > 0:
                    for group in groups_ge_3:
                        group.update(joker_stack.pop())
                        if len(joker_stack) == 0:
                            break

        return groups_ge_3

    def get_groups(self):
        values = self.value_sort()
        sets = [set(values[i]) for i in range(1, len(values)) if len(values[i]) > 0]
        groups = self.place_jokers_in_groups(sets, values)
        
        return groups

    def get_runs(self):
        pass

    def get_sets(self):
        pass

