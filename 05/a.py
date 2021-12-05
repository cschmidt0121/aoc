import re

f = open("input.txt", "r")
data = f.read().splitlines()
lines = []
for line in data:
    search = re.findall(r'(\d+)', line)
    x1, y1, x2, y2 = int(search[0]), int(search[1]), int(search[2]), int(search[3])

    lines.append([x1, y1, x2, y2])

grid = []

# initialize grid
for row in range(0, 1000):
    grid.append([])
    for column in range(0, 1000):
        grid[row].append(0)


for line in lines:
    x1, y1, x2, y2 = line[0], line[1], line[2], line[3]
    if not (x1 == x2 or y1 == y2):
        continue
    if x1 == x2:
        if y2 > y1:
            start = y1
            end = y2
        else:
            start = y2
            end = y1
        for i in range(start, end + 1):
            grid[x1][i] += 1
    elif y1 == y2:
        if x2 > x1:
            start = x1
            end = x2
        else:
            start = x2
            end = x1
        for i in range(start, end + 1):
            grid[i][y1] += 1

count = 0
for column in range(0, len(grid)):
    for row in range(0, len(grid[0])):
        if grid[row][column] >= 2:
            count += 1

print(count)