"""Dojo 2022-08-17."""


def high_and_low0(seq: str) -> str:
    """Problema 1."""
    maximo, minimo = -1e1000, +1e1000

    new_seq: list[int] = [int(x) for x in seq.split()]
    for i in new_seq:
        if i > maximo:
            maximo = i
        if i < minimo:
            minimo = i
    return f'{maximo} {minimo}'


def high_and_low(seq: str) -> str:
    """Problema 1."""
    nseq = [int(x) for x in seq.split()]
    return f'{max(nseq)} {min(nseq)}'


# Custo computacional
#
# ipython -i dojo
# >>> from dis import dis
#


def mysort0(a: float, b: float, c: float) -> tuple:
    """Problema 2.

    # a < b < c
    """
    if c < a:
        c, a = a, c
    if c < b:
        c, b = b, c
    if b < a:
        b, a = a, b
    return c, b, a


def mysort1(a: float, b: float, c: float) -> tuple:
    """Problema 2."""
    result = [a, b, c]
    result.sort(reverse=True)
    return tuple(result)


def mysort(a: float, b: float, c: float) -> tuple:
    """Problema 2."""
    return tuple(sorted((a, b, c), reverse=True))
