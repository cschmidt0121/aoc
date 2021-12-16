with open("input.txt", "r") as f:
    lines = f.read().splitlines()


def find_adjacents(x, y):
    value = grid[y][x]
    adjacent_coords = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
    validated_coords = []
    for coord in adjacent_coords:
        v_y, v_x = coord
        if v_y < 0 or v_y > (len(grid[0]) - 1) or v_x < 0 or v_x > len(grid) - 1:
            continue
        validated_coords.append(coord)
    return validated_coords


def smallest_tentative_distance(coords, distance_grid):
    smallest_x, smallest_y = coords[0]
    for x, y in coords:
        if distance_grid[x][y] < distance_grid[smallest_x][smallest_y]:
            smallest_x = x
            smallest_y = y
    return [smallest_x, smallest_y]


def calculate_total_risk(initial, final, previous):
    total = 0
    current_x, current_y = final
    visited = []
    while [current_x, current_y] != initial:
        total += grid[current_x][current_y]
        visited.append([current_x, current_y])
        current_x, current_y = previous[(current_x, current_y)]
    return total


grid = []
for line in lines:
    row = []
    for c in line:
        row.append(int(c))
    grid.append(row)


# transpose
grid = [[grid[y][x] for y in range(len(grid))] for x in range(len(grid[0]))]

# distance grid for Djikstra's
distance_grid = [[9999999999 for x in range(len(grid))] for y in range(len(grid[0]))]
distance_grid[0][0] = 0

unvisited = [[x, y] for x in range(len(grid)) for y in range(len(grid[0]))]

destination = [len(grid) - 1, len(grid[0]) - 1]
previous_nodes = {}
while destination in unvisited:
    current_x, current_y = smallest_tentative_distance(unvisited, distance_grid)
    current_distance = distance_grid[current_x][current_y]
    neighbors = find_adjacents(current_x, current_y)
    for neighbor_x, neighbor_y in neighbors:

        if (current_distance + grid[neighbor_x][neighbor_y]) < distance_grid[
            neighbor_x
        ][neighbor_y]:
            distance_grid[neighbor_x][neighbor_y] = (
                current_distance + grid[neighbor_x][neighbor_y]
            )
            previous_nodes[(neighbor_x, neighbor_y)] = [current_x, current_y]
    unvisited.remove([current_x, current_y])

total = calculate_total_risk([0, 0], destination, previous_nodes)
print(total)
