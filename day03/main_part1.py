from operator import is_
import re


def number_adjacent_to_symbol(input_lines, line_index, start_index, end_index):
    current_line = input_lines[line_index]
    number_length = end_index - start_index
    # To the left
    if start_index > 0 and current_line[start_index - 1] != ".":
        return True
    # To the right
    if end_index < len(current_line) and current_line[end_index] != ".":
        return True
    # Above
    if (
        line_index > 0
        and input_lines[line_index - 1][start_index:end_index] != "." * number_length
    ):
        return True
    # Below
    if (
        line_index < len(input_lines) - 1
        and input_lines[line_index + 1][start_index:end_index] != "." * number_length
    ):
        return True
    # Diagonally above left
    if (
        line_index > 0
        and start_index > 0
        and input_lines[line_index - 1][start_index - 1] != "."
    ):
        return True
    # Diagonally above right
    if (
        line_index > 0
        and end_index < len(current_line)
        and input_lines[line_index - 1][end_index] != "."
    ):
        return True
    # Diagonally below left
    if (
        line_index < len(input_lines) - 1
        and start_index > 0
        and input_lines[line_index + 1][start_index - 1] != "."
    ):
        return True
    # Diagonally below right
    if (
        line_index < len(input_lines) - 1
        and end_index < len(current_line)
        and input_lines[line_index + 1][end_index] != "."
    ):
        return True
    return False


file = open("input.txt", "r")
input_text = file.read()
file.close()

regex = re.compile(r"\d+")

input_lines = input_text.splitlines()

sum_adjacent = 0
for line_index, line in enumerate(input_lines):
    matches = regex.finditer(line)

    for match in matches:
        number = int(match.group())
        start_index = match.start()
        end_index = match.end()

        is_adjacent = number_adjacent_to_symbol(
            input_lines, line_index, start_index, end_index
        )
        if is_adjacent:
            sum_adjacent += number

print(sum_adjacent)
