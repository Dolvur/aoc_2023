import re

file = open("input.txt", "r")
input_text = file.read()
file.close()

MAX_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

regex = re.compile(r"(\d+)\s(red|blue|green)")

sum_possible_games = 0
for index, line in enumerate(input_text.splitlines()):
    game_index = index + 1

    possible_game = True
    for match in regex.finditer(line):
        number = int(match.group(1))
        color = match.group(2)

        if number > MAX_CUBES[color]:
            possible_game = False
            break

    if possible_game:
        sum_possible_games += game_index

print(sum_possible_games)
