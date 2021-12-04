from sys import stdin

binary_length = 12

if __name__ == '__main__':
    _count = [0] * binary_length
    _len = 0
    for line in stdin:
        _bin = list(line.strip())

        for i, b in enumerate(_bin):
            if(b == '1'):
                _count[i] += 1
        
        _len += 1


    _gamma = []
    _epsilon = []
    for c in _count:
        a = '0'
        b = '1'
        if c > _len // 2:
            a = '1'
            b = '0'

        _gamma.append(a)
        _epsilon.append(b)

    print(int("".join(_gamma), 2) * int("".join(_epsilon), 2))