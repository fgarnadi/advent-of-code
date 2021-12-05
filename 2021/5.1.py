from sys import stdin

diagram_size = 1000

if __name__ == '__main__':
    overlap_count = 0
    diagram = [[0 for _ in range(diagram_size)] for _ in range(diagram_size)]

    for line in stdin:
        p1, _, p2 = line.strip().split()
        x1, y1 = map(int, p1.split(','))
        x2, y2 = map(int, p2.split(','))

        # vertical
        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for y in range(y1, y2+1):
                # check first overlap
                if diagram[x1][y] == 1:
                    overlap_count += 1
                
                diagram[x1][y] += 1

        # horizontal
        if y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            for x in range(x1, x2+1):
                # check first overlap
                if diagram[x][y1] == 1:
                    overlap_count += 1
                
                diagram[x][y1] += 1

    print(overlap_count)
        