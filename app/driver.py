from classes.pool import Pool
from classes.tile import Tile
from collections import Counter
import random

class Scenario():
    def __init__(self):
        self.pool = Pool()

    def generate_hand(self, amount=14):
        hand = []
        for _ in range(0, amount):
            tile = random.choice(self.pool.available_tiles())
            tile.available = False
            hand.append(tile)
        return hand

def get_first_set(tiles_in_hand, barrier=30):
    all_sets = get_sets(tiles_in_hand)
    if sum(list(map(sum, all_sets))) >= barrier:
        return all_sets
    else:
        return False

def get_sets(tiles):
    get_groups(tiles)
    get_runs(tiles)
    pass

def get_groups(tiles):
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

def get_runs(tiles):
    sets = [[] for _ in range(14)]
    colors = {
        'BLACK': [],
        'BLUE': [],
        'ORANGE': [],
        'RED': [],
        'NONE': []
    }

    for tile in tiles:
        colors[tile.color.name].append(tile)

    

scenario = Scenario()
my_hand = scenario.generate_hand()
get_sets(my_hand)

my_hand.append(Tile(0,0))
print(my_hand)