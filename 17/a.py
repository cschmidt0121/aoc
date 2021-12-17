import re

with open("input.txt", "r") as f:
    data = f.read()

x_min, x_max, y_min, y_max = re.findall("x=(-?\d+)\.\.(-?\d+).*y=(-?\d+)\.\.(-?\d+)", data)[0]
x_min = int(x_min)
x_max = int(x_max)
y_min = int(y_min)
y_max = int(y_max)

def is_valid_initial_velocity(initial_x, initial_y, x_min, x_max, y_min, y_max):
    step = 0
    position_x = position_y = 0
    velocity_x = initial_x
    velocity_y = initial_y

    max_height = 0
    while True:
        position_x += velocity_x
        position_y += velocity_y
        if velocity_x > 0:
            velocity_x -= 1
        elif velocity_x < 0:
            velocity_x += 1

        velocity_y -= 1
        max_height = position_y if position_y > max_height else max_height
        if position_x > x_max and position_y < y_min:
            return None
        if velocity_x == 0 and position_y < y_min:
            return None
        if position_x >= x_min and position_x <= x_max and position_y >= y_min and position_y <= y_max:
            valid = True
            return max_height

best_height = 0
best_x = best_y = 0

for initial_x in range(0, 500):
    for initial_y in range(0, 500):
        result = is_valid_initial_velocity(initial_x, initial_y, x_min, x_max, y_min, y_max)

        if result and result > best_height:
            best_x = initial_x
            best_y = initial_y
            best_height = result
print(best_x, best_y)
print(best_height)

