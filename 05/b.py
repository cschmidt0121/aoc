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


def print_grid():
    """ Print the grid to compare against sample for debugging"""
    for column in range(0, len(grid)):
        r_str = ""
        for row in range(0, len(grid[0])):
            r_str += " " + str(grid[row][column]) + " "
        print(r_str)


for line in lines:
    x1, y1, x2, y2 = line[0], line[1], line[2], line[3]
    if not (x1 == x2 or y1 == y2):
        """ Diagonal line """
        length = abs((x2 - x1)) + 1 # Can do this because 45 degree
        if x2 > x1:
            x_increasing = True
        else:
            x_increasing = False
        if y2 > y1:
            y_increasing = True
        else:
            y_increasing = False

        cursor_x = x1
        cursor_y = y1

        for i in range(0, length):
            grid[cursor_x][cursor_y] += 1
            cursor_x = cursor_x + 1 if x_increasing else cursor_x - 1
            cursor_y = cursor_y + 1 if y_increasing else cursor_y - 1

    """ Horizontal line """
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
    #print_grid()

count = 0
for column in range(0, len(grid)):
    for row in range(0, len(grid[0])):
        if grid[row][column] >= 2:
            count += 1

print(count)

