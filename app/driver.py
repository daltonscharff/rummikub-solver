from classes import Pool, Tile
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


# my_hand = generate_hand()
example = [Tile(2, 1), Tile(3, 1), Tile(4, 2), Tile(2, 3), Tile(1, 3), Tile(4, 3), Tile(4, 5)]
my_hand = Pool(example)

print(f"Hand:\t{my_hand.tiles}")
print(f"Groups:\t{my_hand.get_groups()}")
print(f"Runs:\t{my_hand.get_runs()}")