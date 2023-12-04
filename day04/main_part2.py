file = open("input.txt", "r")
input_text = file.read()
file.close()

input_lines = input_text.splitlines()

num_of_cards = {key: 1 for key in range(len(input_lines))}

for line_index, line in enumerate(input_lines):
    line = line.split(":")[1]
    winning_numbers, own_numbers = line.split("|")
    winning_numbers = [int(x.strip()) for x in winning_numbers.split(" ") if x.strip()]
    own_numbers = [int(x.strip()) for x in own_numbers.split(" ") if x.strip()]

    # Check how many numbers are correct
    correct_numbers = 0
    for number in own_numbers:
        if number in winning_numbers:
            correct_numbers += 1

    for i in range(correct_numbers):
        next_index = line_index + i + 1
        num_of_cards[next_index] += num_of_cards[line_index]

# Sum of all cards
print(sum(num_of_cards.values()))
