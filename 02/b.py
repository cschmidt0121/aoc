h = 0
d = 0
aim = 0

f = open("input.txt", "r")
data = f.read()
lines = data.splitlines()
for line in lines:
    instruction, val = line.split(" ")
    if instruction == "forward":
        h += int(val)
        d += aim * int(val)
    elif instruction == "down":
        aim += int(val)
    elif instruction == "up":
        aim -= int(val)

print(d*h)
