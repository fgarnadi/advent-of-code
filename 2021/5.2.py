from sys import stdin

diagram_size = 1000

if __name__ == '__main__':
    overlap_count = 0
    diagram = [[0 for _ in range(diagram_size)] for _ in range(diagram_size)]
    
    for line in stdin:
        p1, _, p2 = line.strip().split()
        x1, y1 = map(int, p1.split(','))
        x2, y2 = map(int, p2.split(','))

        x_mod = 0
        y_mod = 0

        if x1 > x2:
            x_mod = -1
        elif x1 < x2:
            x_mod = 1

        if y1 > y2:
            y_mod = -1
        elif y1 < y2:
            y_mod = 1

        while(x1 != x2+x_mod or y1 != y2+y_mod):
            if diagram[x1][y1] == 1:
                overlap_count += 1
                
            diagram[x1][y1] += 1

            x1 += x_mod
            y1 += y_mod

    print(overlap_count)
        
