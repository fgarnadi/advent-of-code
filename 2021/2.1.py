from sys import stdin
from functools import reduce

if __name__ == '__main__':
    _move_h = {
        'forward' : 1
    }

    _move_v = {
        'down' : 1,
        'up' : -1
    }

    # horizontal, depth
    pos = [0, 0]
    for line in stdin:
        act, step = line.split()
        step = int(step)

        pos[0] += _move_h.get(act, 0) * step
        pos[1] += _move_v.get(act, 0) * step

    print(reduce(lambda a, b: a * b, pos))