with open("input.txt", "r") as f:
    lines = f.read().splitlines()

grid = []
for line in lines:
    row = []
    for c in line:
        row.append(int(c))
    grid.append(row)

FLASH_COUNT = 0


def find_adjacents(y, x):
    value = grid[y][x]
    adjacent_coords = [[y, x-1], [y, x+1], [y-1, x], [y+1, x], [y-1, x-1], [y-1, x+1], [y+1, x+1], [y+1, x-1]]
    validated_coords = []
    for coord in adjacent_coords:
        v_y, v_x = coord
        if v_y < 0 or v_y > (len(grid) - 1) or v_x < 0 or v_x > len(grid[0]) - 1:
            continue
        validated_coords.append(coord)
    return validated_coords


def flash(y, x, grid, already_flashed):
    global FLASH_COUNT
    FLASH_COUNT += 1
    already_flashed.append([y, x])
    adjacent_coords = find_adjacents(y, x)
    for i, adjacent_coord in enumerate(adjacent_coords):
        if adjacent_coord in already_flashed:
            continue
        adjacent_y, adjacent_x = adjacent_coord
        grid[adjacent_y][adjacent_x] += 1
        if grid[adjacent_y][adjacent_x] > 9:
            grid, already_flashed = flash(adjacent_y, adjacent_x, grid, already_flashed)

    return grid, already_flashed


def do_step(grid):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            grid[y][x] += 1
    flashed = []
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] > 9 and [y, x] not in flashed:
                grid, flashed = flash(y, x, grid, flashed)

    for coord in flashed:
        f_y, f_x = coord
        grid[f_y][f_x] = 0

    return grid


def print_board(grid):
    for line in grid:
        print(line)


for i in range(0, 100):
    do_step(grid)


print(FLASH_COUNT)