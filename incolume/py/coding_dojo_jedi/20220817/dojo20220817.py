"""Dojo 2022-08-17."""


def high_and_low0(seq: str) -> str:
    """Problema 1."""
    maximo, minimo = -1e1000, +1e1000

    seq = [int(x) for x in seq.split()]
    for i in seq:
        if i > maximo:
            maximo = i
        if i < minimo:
            minimo = i
    return f'{maximo} {minimo}'


def high_and_low(seq: str) -> str:
    """Problema 1."""
    seq = [int(x) for x in seq.split()]
    return f'{max(seq)} {min(seq)}'


# Custo computacional
#
# ipython -i dojo
# >>> from dis import dis
#
# dis(mysort0)
# dis(mysort1)
# dis(mysort)


def mysort0(a, b, c):
    """Problema 2.

    # a < b < c
    """
    if c < a:
        c, a = a, c
    if c < b:
        c, b = b, c
    if b < a:
        b, a = a, b
    return (c, b, a)


def mysort1(a, b, c):
    """Problema 2."""
    result = [a, b, c]
    result.sort(reverse=True)
    return tuple(result)


def mysort(a, b, c):
    """Problema 2."""
    return tuple(sorted((a, b, c), reverse=True))
