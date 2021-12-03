f = open("input.txt", "r")
data = f.read()
oxygen_lines = data.splitlines()
f = open("input.txt", "r")
data = f.read()
co2_lines = data.splitlines()

iteration = 0

oxygen = None
while True:
    zero_count = 0
    one_count = 0
    for line in oxygen_lines:
        char = line[iteration]
        if char == "0":
            zero_count += 1
        else:
            one_count += 1
    new_lines = []
    for line in oxygen_lines:
        char = line[iteration]
        if (char == "0" and zero_count > one_count) or (char == "1" and ((one_count > zero_count) or one_count == zero_count)):
            new_lines.append(line)
    if len(new_lines) == 1:
        oxygen = int(new_lines[0], 2)
        print(f"Oxygen generator rating: {oxygen}")
        break
    iteration += 1
    oxygen_lines = new_lines

co2 = None
iteration = 0
while True:
    zero_count = 0
    one_count = 0
    for line in co2_lines:
        char = line[iteration]
        if char == "0":
            zero_count += 1
        else:
            one_count += 1
    new_lines = []
    for line in co2_lines:
        char = line[iteration]
        if (char == "0" and (zero_count < one_count or (one_count == zero_count))) or (char == "1" and (one_count < zero_count) ):
            new_lines.append(line)
    if len(new_lines) == 1:
        co2 = int(new_lines[0], 2)
        print(f"C02 scrubber rating: {co2}")
        break
    iteration += 1
    co2_lines = new_lines

print(f"Answer is: {oxygen * co2}")