import math


file = open("input.txt", "r")
input_text = file.read()
file.close()

lines = input_text.strip().split("\n")
values = [list(map(int, filter(bool, line.split(" ")[1:]))) for line in lines]

time = int("".join(map(str, values[0])))
dist_to_beat = int("".join(map(str, values[1])))

SMALL_FACTOR = 0.01  # Don't allow for ties

permutations_to_win = 1
min_root = math.ceil(time / 2 - math.sqrt(time**2 / 4 - dist_to_beat) + SMALL_FACTOR)
max_root = math.floor(time / 2 + math.sqrt(time**2 / 4 - dist_to_beat) - SMALL_FACTOR)
ways_to_win = max_root - min_root + 1
permutations_to_win *= ways_to_win

print(permutations_to_win)
