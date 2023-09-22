"""Dojo."""


from typing import List


def razao(seq: List):
    """Calcula a razão."""
    if len(seq) == 1:
        return seq[-1]
    return seq[-1] - seq[-2]


def validate(fizz, buzz, fizzbuzz):
    """Valida resultado fizzbuzz."""
    if fizz and buzz:
        return [razao(fizz), razao(buzz)]
    if not fizz and not buzz:
        return [razao(fizzbuzz)] * 2
    if fizz and fizzbuzz:
        return [razao(fizz), razao(fizzbuzz)]
    if buzz and fizzbuzz:
        return [razao(buzz), razao(fizzbuzz)]
    return None


def fizz_buzz_backwards(seq: List):
    """Aplica validação fizzbuzz a lista."""
    if len(seq) > 100:
        msg = 'Comprimento máximo de 100 elementos.'
        raise OverflowError(msg)
    fizz, buzz, fizzbuzz = [], [], []
    for i, x in enumerate(seq, 1):
        if str(x).casefold() == 'fizz':
            fizz.append(i)
        elif str(x).casefold() == 'buzz':
            buzz.append(i)
        elif str(x).casefold() == 'fizzbuzz':
            fizzbuzz.append(i)

    return validate(fizz, buzz, fizzbuzz)
