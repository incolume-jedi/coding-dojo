"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'  # pragma: no cover

from itertools import count


def is_prime(num: int) -> bool:
    """Check if prime number."""
    num = abs(num)
    if num <= 1:
        return False
    return all(num % n != 0 for n in range(2, num // 2 + 1))


def gen_4prime():
    """Gerador de primos com 4 algarismos."""
    c = count(10 * 3 + 1, step=2)
    algarismos = 4
    while len(str(num := next(c))) < algarismos + 1:
        if is_prime(num) and len(str(num)) == algarismos:
            yield num
