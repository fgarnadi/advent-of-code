from sys import stdin

binary_length = 12

if __name__ == '__main__':
    count = [0] * binary_length
    _len = 0
    for line in stdin:
        _bin = list(line.strip())

        for i, b in enumerate(_bin):
            if(b == '1'):
                count[i] += 1
        
        _len += 1


    gamma = []
    epsilon = []
    for c in count:
        a = '0'
        b = '1'
        if c > _len // 2:
            a = '1'
            b = '0'

        gamma.append(a)
        epsilon.append(b)

    print(int("".join(gamma), 2) * int("".join(epsilon), 2))