from sys import stdin
from functools import reduce

octopuses = []
max_x = 0
max_y = 0

step = 100
light_count = 0


def chain_light(y, x):
    global max_x, max_y, octopuses, light_count

    if x >= max_x or x < 0:
        return
    if y >= max_y or y < 0:
        return

    if octopuses[y][x] < 0:
        return

    if octopuses[y][x] < 10:
        octopuses[y][x] += 1

    if octopuses[y][x] == 10:
        light_count += 1
        octopuses[y][x] = -1

        chain_light(y - 1, x)  # up
        chain_light(y + 1, x)  # down
        chain_light(y, x - 1)  # left
        chain_light(y, x + 1)  # right
        chain_light(y - 1, x - 1)  # up-left
        chain_light(y - 1, x + 1)  # up-right
        chain_light(y + 1, x - 1)  # down-left
        chain_light(y + 1, x + 1)  # down-right


if __name__ == "__main__":
    for line in stdin:
        octopuses.append(list(map(int, list(line.strip()))))

    max_x = len(octopuses[0])
    max_y = len(octopuses)

    for _ in range(step):
        for y in range(max_y):
            for x in range(max_x):
                if octopuses[y][x] < 0:
                    octopuses[y][x] = 0

                octopuses[y][x] += 1

        for y in range(max_y):
            for x in range(max_x):
                if octopuses[y][x] == 10:
                    chain_light(y, x)

    print(light_count)
