from sys import stdin
from functools import reduce

max_x = 0
max_y = 0

caves = []
shadow_caves = []


def traverse_basin(y, x):
    global max_x, max_y, caves, shadow_caves

    if x >= max_x or x < 0:
        return 0
    if y >= max_y or y < 0:
        return 0

    if shadow_caves[y][x] == 1 or caves[y][x] == 9:
        return 0

    shadow_caves[y][x] = 1

    return (
        1
        + traverse_basin(y - 1, x)  # up
        + traverse_basin(y + 1, x)  # down
        + traverse_basin(y, x - 1)  # left
        + traverse_basin(y, x + 1)  # right
    )


if __name__ == "__main__":
    caves = []
    for line in stdin:
        caves.append(list(map(int, list(line.strip()))))

    max_x = len(caves[0])
    max_y = len(caves)

    shadow_caves = [[0 for _ in range(max_x)] for _ in range(max_y)]
    basin_sizes = []
    for y in range(max_y):
        for x in range(max_x):
            up = True
            down = True
            left = True
            right = True

            # check left
            if x > 0 and caves[y][x] >= caves[y][x - 1]:
                left = False

            # check down
            if y < max_y - 1 and caves[y][x] >= caves[y + 1][x]:
                down = False

            # check right
            if x < max_x - 1 and caves[y][x] >= caves[y][x + 1]:
                right = False

            # check up
            if y > 0 and caves[y][x] >= caves[y - 1][x]:
                up = False

            if up and right and down and left:
                basin_sizes.append(traverse_basin(y, x))

    print(reduce(lambda a, b: a * b, sorted(basin_sizes)[-3:]))
