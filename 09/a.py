with open("input.txt", "r") as f:
    lines = f.read().splitlines()

grid = []
for line in lines:
    row = []
    for c in line:
        row.append(int(c))
    grid.append(row)

total_risk = 0
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        value = grid[y][x]
        adjacent_vals = []
        if (x - 1) >= 0:
            adjacent_vals.append(grid[y][x - 1])
        if (x + 1) < len(grid[0]):
            adjacent_vals.append(grid[y][x + 1])
        if (y - 1) >= 0:
            adjacent_vals.append(grid[y - 1][x])
        if (y + 1) < len(grid):
            adjacent_vals.append(grid[y + 1][x])
        if all(value < adjacent_val for adjacent_val in adjacent_vals):
            total_risk += 1 + value

print(total_risk)
