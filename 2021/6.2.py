from sys import stdin
from collections import Counter

# represent fish life timer
pool_size = 9

days = 256

if __name__ == '__main__':
    initial = map(int, str(input()).split(','))
    fishes = dict(Counter(initial))

    for _ in range(days):
        prev = 0
        for i in range(pool_size-1, -1, -1):
            fishes[i] = fishes.get(i, 0)
            if i == 0:
                fishes[6] = fishes.get(6) + fishes.get(0)
                fishes[8] = fishes.get(0)
                fishes[0] = prev
            else:
                prev, fishes[i] = fishes.get(i), prev

    print(sum(x for x in fishes.values()))
        