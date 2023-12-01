import re

file = open("input.txt", "r")
input_text = file.read()
file.close()

digit_dict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
pattern = r"(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))"
total_sum = 0
for line in input_text.splitlines():
    matches = re.findall(pattern, line)
    if matches:
        first_digit = matches[0]
        last_digit = matches[-1]

        # print("==== NEW LINE ====")
        # print(line)
        # print(first_digit, last_digit)

        if len(first_digit) > 1:
            first_digit = digit_dict[first_digit]

        if len(last_digit) > 1:
            last_digit = digit_dict[last_digit]

        local_sum = int(str(first_digit) + str(last_digit))
        # print("local sum: ", local_sum)
        total_sum += local_sum
    else:
        raise Exception("No matches found on line: ", line)

print(total_sum)
