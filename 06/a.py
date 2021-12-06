with open("input.txt", "r") as f:
    data=f.read().split(",")
fish = [int(val) for val in data]

day = 0
days = 80

while day < days:
    next_fish = [] 
    for f in fish:
        if f == 0:
            next_fish.append(6)
            next_fish.append(8)
        else:
            next_fish.append(f - 1)
    day += 1
    fish = next_fish

print(len(fish))
