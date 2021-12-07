f = open("input.txt", "r")
crabs = [int(item) for item in f.read().split(",")]
farthest = max(crabs)

lowest_fuel = 999999999
lowest_fuel_position = None
for i in range(0, max(crabs) + 1):
    fuel_cost = 0
    for c in crabs:
        fuel_cost += abs(c - i)
    if fuel_cost < lowest_fuel:
        lowest_fuel = fuel_cost
        lowest_fuel_position = i

print(lowest_fuel, lowest_fuel_position)