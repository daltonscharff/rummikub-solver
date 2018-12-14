from classes.pool import Pool
from classes.tile import Tile
from collections import Counter
import random

def generate_hand(pool=Pool(), amount=14):
    hand = []
    for _ in range(0, amount):
        tile = random.choice(pool.available_tiles())
        tile.available = False
        hand.append(tile)
    return Pool(hand)

# def get_first_set(tiles_in_hand, barrier=30):
#     all_sets = get_sets(tiles_in_hand)
#     if sum(list(map(sum, all_sets))) >= barrier:
#         return all_sets
#     else:
#         return False


my_hand = generate_hand()

print(f"Hand:\t{my_hand.tiles}")
print(f"Groups:\t{my_hand.get_groups()}")
print(f"Runs:\t{my_hand.get_runs()}")