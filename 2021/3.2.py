from sys import stdin

binary_length = 12

if __name__ == '__main__':
    _lines = []
    for line in stdin:
        _bin = list(line.strip())
        _lines.append(_bin)

    _oxy = _lines
    _co2 = _lines

    for i in range(binary_length):
        _oxy_c = sum([int(x[i]) for x in _oxy])
        _val_oxy = '1'
        _len_oxy = len(_oxy)
        if(_oxy_c < (_len_oxy - _oxy_c)):
            _val_oxy = '0'

        if _len_oxy > 1:
            _oxy = list(filter(lambda x: x[i] == _val_oxy, _oxy))

        _co2_c = sum([int(x[i]) for x in _co2])
        _val_co2 = '0'
        _len_co2 = len(_co2)
        if(_co2_c < (_len_co2 - _co2_c)):
            _val_co2 = '1'

        if _len_co2 > 1:
            _co2 = list(filter(lambda x: x[i] == _val_co2, _co2))

    print(int("".join(_oxy[0]), 2) * int("".join(_co2[0]), 2))