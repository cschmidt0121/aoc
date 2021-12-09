from functools import reduce

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

grid = []
for line in lines:
    row = []
    for c in line:
        row.append(int(c))
    grid.append(row)


def measure_basin(y, x, measured_basin_coords):
    current_value = grid[y][x]
    adjacent_coords, adjacent_vals = find_adjacents(y, x)

    basin_coords = []
    basin_vals = []
    for i, val in enumerate(adjacent_vals):
        if val > current_value and val != 9:
            basin_coords.append(adjacent_coords[i])
            basin_vals.append(adjacent_vals[i])

    if len(basin_vals) == 0:
        return 1
    else:
        basin_size = 1
        for coord in basin_coords:
            if coord in measured_basin_coords:
                continue
            measured_basin_coords.append(coord)
            basin_size += measure_basin(coord[0], coord[1], measured_basin_coords)
        return basin_size


def find_adjacents(y, x):
    value = grid[y][x]
    adjacent_vals = []
    adjacent_coords = []
    if (x - 1) >= 0:
        adjacent_vals.append(grid[y][x - 1])
        adjacent_coords.append([y, x - 1])
    if (x + 1) < len(grid[0]):
        adjacent_vals.append(grid[y][x + 1])
        adjacent_coords.append([y, x + 1])
    if (y - 1) >= 0:
        adjacent_vals.append(grid[y - 1][x])
        adjacent_coords.append([y - 1, x])
    if (y + 1) < len(grid):
        adjacent_vals.append(grid[y + 1][x])
        adjacent_coords.append([y + 1, x])
    return (adjacent_coords, adjacent_vals)


basin_sizes = []
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        value = grid[y][x]
        adjacent_coords, adjacent_vals = find_adjacents(y, x)
        if all(value < adjacent_val for adjacent_val in adjacent_vals):
            size = measure_basin(y, x, [[y, x]])
            basin_sizes.append(size)

answer = reduce((lambda x, y: x * y), sorted(basin_sizes, reverse=True)[0:3])

print(answer)
