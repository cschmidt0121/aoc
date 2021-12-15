import re

def fold(grid, coord, value):
    if coord == "y":
        new_grid = [[0 for i in range(0, value)] for i in range(0, len(grid))]
        for x in range(0, len(grid)):
            for y in range(0, value):
                new_grid[x][y] = grid[x][y]
        for x in range(0, len(grid)):
            for y in range(value+1, len(grid[0])):
                old_value = grid[x][y]
                if old_value != 0:
                    new_grid[x][abs(y-value*2)] = old_value
    else:
        new_grid = [[0 for i in range(0, len(grid[0]))] for i in range(0, value)]
        for x in range(0, value):
            for y in range(0, len(grid[0])):
                new_grid[x][y] = grid[x][y]
        for x in range(value+1, len(grid)):
            for y in range(0, len(grid[0])):
                old_value = grid[x][y]
                if old_value != 0:
                    new_grid[abs(x-value*2)][y] = old_value
    return new_grid

def count_dots(grid):
    return sum(map(sum, grid))

def print_grid(grid):
    for y in range(0, len(grid[0])):
        line = ""
        for x in range(0, len(grid)):
            val = grid[x][y]
            if val == 1:
                line += "#"
            else:
                line += " "
        print(line + "\n")

f = open("input.txt", "r")

line = f.readline()
max_x = 0
max_y = 0
points = []
while line != "\n":
    x, y = map(int, line.split(","))
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    points.append([x,y])
    line = f.readline()

folds = []
for fold_line in f.readlines():
    coord, value = re.findall("([yx])=(\d+)", fold_line)[0]
    folds.append([coord, int(value)])

grid = [[0 for i in range(0, max_y+1)] for i in range(0, max_x+1)]

for point in points:
    x, y = point
    grid[x][y] = 1

#print_grid(grid)
for f in folds:
    grid = fold(grid, f[0], f[1])
    #break

print(count_dots(grid))
print_grid(grid)