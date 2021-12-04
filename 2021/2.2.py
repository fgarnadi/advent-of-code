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

    # horizontal, depth, aim
    pos = [0, 0, 0]
    for line in stdin:
        act, step = line.split()
        step = int(step)

        if(_move := _move_h.get(act, 0) != 0):
            pos[0] += _move * step
            pos[1] += pos[2] * step

        pos[2] += _move_v.get(act, 0) * step

    print(reduce(lambda a, b: a * b, pos[:2]))