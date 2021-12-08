from sys import stdin
from collections import Counter

# real spaghetti :-


def signal_map(signal):
    number_map = {
        "123567": 0,
        "36": 1,
        "13457": 2,
        "13467": 3,
        "2346": 4,
        "12467": 5,
        "124567": 6,
        "136": 7,
        "1234567": 8,
        "123467": 9,
    }
    signal_set = list(map(lambda s: Counter(s), signal))
    signal_list = {}
    signal_dict = {}
    segment = {}

    # count and group the signal
    for s in signal_set:
        key = len(s)
        signal_dict[key] = signal_dict.get(key, Counter())
        signal_dict[key] += s

        signal_list[key] = signal_list.get(key, [])
        signal_list[key].append(set(s))

    # get the intersection
    for key in signal_dict.keys():
        signal_dict[key] = dict(signal_dict[key])
        _max = max(signal_dict[key].values())

        new_el = []
        for inner_key in signal_dict[key].keys():
            if signal_dict[key][inner_key] != _max or _max == 1:
                new_el.append(inner_key)

        signal_dict[key] = set(new_el)

    # apply the formula
    segment[1] = signal_dict.get(3) - signal_dict.get(2)
    segment[2] = signal_dict.get(5) & signal_dict.get(4) - signal_dict.get(2)
    segment[3] = signal_dict.get(2)
    segment[4] = signal_dict.get(4) - signal_dict.get(2) - segment[2]
    segment[5] = (
        signal_dict.get(7)
        - (signal_dict.get(2) | signal_dict.get(3) | signal_dict.get(4))
        & signal_dict.get(6)
        & signal_dict.get(5)
    )
    segment[6] = signal_dict.get(2)
    segment[7] = (
        signal_dict.get(7)
        - (signal_dict.get(2) | signal_dict.get(3) | signal_dict.get(4))
        - segment[5]
    )

    # get number 6
    for _dict in signal_list[6]:
        _set = set(_dict) & signal_dict.get(2)
        if len(_set) == 1:
            segment[6] = _set
            segment[3] = segment[3] - _set

    segment_rev = {list(segment[k])[0]: k for k in segment.keys()}
    ret = {}
    for sig in signal:
        key = "".join(sorted([str(segment_rev[s]) for s in sig]))
        ret["".join(sorted(sig))] = number_map[key]

    return ret


if __name__ == "__main__":

    _sum = 0
    for line in stdin:
        signal, output = map(lambda x: x.strip().split(), line.split("|"))

        _map = signal_map(signal)
        _sum += int("".join([str(_map["".join(sorted(out))]) for out in output]))

    print(_sum)
