from queue import PriorityQueue


def find_adjacents(x, y, grid):
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


def calculate_total_risk(initial, final, previous, grid):
    total = 0
    current_x, current_y = final
    visited = []
    while [current_x, current_y] != initial:
        total += grid[current_x][current_y]
        visited.append([current_x, current_y])
        current_x, current_y = previous[(current_x, current_y)]
    return total


def generate_full_grid(sample):
    grid = [[0 for x in range(len(sample) * 5)] for y in range(len(sample[0]) * 5)]
    for x in range(len(sample) * 5):
        for y in range(len(sample[0]) * 5):
            tile_x = int(x / len(sample))
            tile_y = int(y / len(sample[0]))
            sample_x = x % len(sample)
            sample_y = y % len(sample[0])
            value = sample[sample_x][sample_y] + (tile_x + tile_y)
            value = ((value - 1) % 9) + 1  # wrap it

            grid[x][y] = value
    return grid


with open("input.txt", "r") as f:
    lines = f.read().splitlines()

sample_grid = []
for line in lines:
    row = []
    for c in line:
        row.append(int(c))
    sample_grid.append(row)


# transpose
sample_grid = [
    [sample_grid[y][x] for y in range(len(sample_grid))]
    for x in range(len(sample_grid[0]))
]
full_grid = generate_full_grid(sample_grid)


# distance grid for Djikstra's
distance_grid = [
    [9999999999 for x in range(len(full_grid))] for y in range(len(full_grid[0]))
]
distance_grid[0][0] = 0

unvisited = PriorityQueue()
for x in range(len(full_grid)):
    for y in range(len(full_grid[0])):
        unvisited.put(item=(9999999999, (x, y)))

destination = [len(full_grid) - 1, len(full_grid[0]) - 1]
previous_nodes = {}
while True:
    current_x, current_y = unvisited.get(timeout=5)[1]
    if [current_x, current_y] == destination:
        break
    current_distance = distance_grid[current_x][current_y]
    neighbors = find_adjacents(current_x, current_y, full_grid)
    for neighbor_x, neighbor_y in neighbors:

        if (current_distance + full_grid[neighbor_x][neighbor_y]) < distance_grid[
            neighbor_x
        ][neighbor_y]:
            distance_grid[neighbor_x][neighbor_y] = (
                current_distance + full_grid[neighbor_x][neighbor_y]
            )
            previous_nodes[(neighbor_x, neighbor_y)] = [current_x, current_y]
            unvisited.put(
                (
                    current_distance + full_grid[neighbor_x][neighbor_y],
                    (neighbor_x, neighbor_y),
                )
            )


total = calculate_total_risk([0, 0], destination, previous_nodes, full_grid)
print(total)
