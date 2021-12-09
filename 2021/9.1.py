from sys import stdin

if __name__ == "__main__":
    caves = []
    for line in stdin:
        caves.append(list(map(int, list(line.strip()))))

    max_x = len(caves[0])
    max_y = len(caves)

    risk_level = 0
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
                risk_level += caves[y][x] + 1

    print(risk_level)
