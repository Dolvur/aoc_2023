file = open("input.txt", "r")
input = file.read()
file.close()

sum = 0
for line in input.splitlines():
    first_digit = None
    last_digit = None
    for i in range(len(line)):
        if first_digit is not None and last_digit is not None:
            break

        if line[i].isdigit():
            if first_digit is None:
                first_digit = line[i]

        if line[-(i + 1)].isdigit():
            if last_digit is None:
                last_digit = line[-(i + 1)]

    sum += int(str(first_digit) + str(last_digit))

print(sum)
