from pool import Pool
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
        
scenario = Scenario()
my_hand = scenario.generate_hand()
print(my_hand)

def get_first_set(barrier=30):
    all_sets = get_all_sets()
    if sum(list(map(sum, all_sets))) >= barrier:
        return all_sets
    else:
        return False

def get_all_sets():
    return []
