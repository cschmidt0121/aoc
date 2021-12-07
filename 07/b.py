from functools import reduce

f = open("input.txt", "r")
crabs = [int(item) for item in f.read().split(",")]
farthest = max(crabs)

lowest_fuel = 999999999
lowest_fuel_position = None


""" Slow way 
for i in range(0, max(crabs) + 1):
    fuel_cost = 0
    for c in crabs:
        fuel_cost += sum([i for i in range(1, abs(c - i) + 1)])
    if fuel_cost < lowest_fuel:
        lowest_fuel = fuel_cost
        lowest_fuel_position = i
"""

""" Faster. thanks Amy """
# Square the number and halve it
def triangle(n):
    return int(n * (n + 1) / 2)

for i in range(0, max(crabs) + 1):
    fuel_cost = sum([triangle(abs(c-i)) for c in crabs])
    if fuel_cost < lowest_fuel:
        lowest_fuel = fuel_cost
        lowest_fuel_position = i

print(f"Lowest fuel: {lowest_fuel}, Position moved to: {lowest_fuel_position}")