from sys import stdin

binary_length = 12

if __name__ == '__main__':
    lines = []
    for line in stdin:
        lines.append(list(line.strip()))

    oxy = lines
    co2 = lines

    for i in range(binary_length):
        oxy_count = sum([int(x[i]) for x in oxy])
        oxy_val = '1'
        oxy_len = len(oxy)
        if(oxy_count < (oxy_len - oxy_count)):
            oxy_val = '0'

        if oxy_len > 1:
            oxy = list(filter(lambda x: x[i] == oxy_val, oxy))

        co2_count = sum([int(x[i]) for x in co2])
        co2_val = '0'
        co2_len = len(co2)
        if(co2_count < (co2_len - co2_count)):
            co2_val = '1'

        if co2_len > 1:
            co2 = list(filter(lambda x: x[i] == co2_val, co2))

    print(int("".join(oxy[0]), 2) * int("".join(co2[0]), 2))