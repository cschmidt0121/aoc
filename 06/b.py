from functools import reduce

with open("input.txt", "r") as f:
    data=f.read().split(",")
fish = [int(val) for val in data]

days = 256

def count_fish(fish, days):
    fish_by_age = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for f in fish:
        fish_by_age[f] += 1

    for i in range(days, 0, -1):
        if fish_by_age[0] > 0:
            fish_by_age[7] += fish_by_age[0]
            fish_by_age[9] += fish_by_age[0]
        fish_by_age = fish_by_age[1:] + [0]

    return reduce(lambda a, b: a+b, fish_by_age)    


print(count_fish(fish, days))
