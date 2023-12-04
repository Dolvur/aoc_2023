file = open("input.txt", "r")
input_text = file.read()
file.close()

points = 0
for line in input_text.splitlines():
    line = line.split(":")[1]
    winning_numbers, own_numbers = line.split("|")
    winning_numbers = [int(x.strip()) for x in winning_numbers.split(" ") if x.strip()]
    own_numbers = [int(x.strip()) for x in own_numbers.split(" ") if x.strip()]

    # Check how many numbers are correct
    correct_numbers = 0
    for number in own_numbers:
        if number in winning_numbers:
            correct_numbers += 1

    if correct_numbers > 0:
        points += 2 ** (correct_numbers - 1)

print(points)
