import re

file = open("input.txt", "r")
input_text = file.read()
file.close()

regex = re.compile(r"(\d+)\s(red|blue|green)")

sum_power_of_sets = 0
for index, line in enumerate(input_text.splitlines()):
    game_index = index + 1

    min_num_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for match in regex.finditer(line):
        number = int(match.group(1))
        color = match.group(2)

        if number > min_num_cubes[color]:
            min_num_cubes[color] = number

    power_of_set = min_num_cubes["red"] * min_num_cubes["green"] * min_num_cubes["blue"]
    sum_power_of_sets += power_of_set

print(sum_power_of_sets)
