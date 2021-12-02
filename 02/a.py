h = 0
d = 0

f = open("input.txt", "r")
data = f.read()
lines = data.splitlines()
for line in lines:
    instruction, val = line.split(" ")
    if instruction == "forward":
        h += int(val)
    elif instruction == "down":
        d += int(val)
    elif instruction == "up":
        d -= int(val)

print(d*h)
