from unittest import result


def high_and_low0(seq: str)->str:
    max, min = -1e1000, +1e1000

    seq = [int(x) for x in seq.split()]
    for i in seq:
        if i > max:
            max = i
        if i < min:
            min = i
    return f'{max} {min}'

def high_and_low(seq: str)->str:
    seq = [int(x) for x in seq.split()]
    return f'{max(seq)} {min(seq)}'
