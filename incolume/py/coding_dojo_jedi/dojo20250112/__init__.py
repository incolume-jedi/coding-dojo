"""dojo module."""

from __future__ import annotations

from functools import lru_cache
from itertools import count


def is_prime_0(num: int | bytes | str) -> bool:
    """Check if prime."""
    try:
        if isinstance(num, float):
            if not (num == int(num)):
                raise ValueError
        num = int(num)
    except (TypeError, ValueError):
        return False

    if num <= 1:
        return False
    for x in range(2, num):  # noqa: SIM110
        if num != 2 and (num % x) == 0:
            return False
    return True


def is_prime_1(num: int | bytes | str) -> bool:
    """Check if prime."""
    try:
        if isinstance(num, float):
            if not (num == int(num)):
                raise ValueError
        num = int(num)
    except (TypeError, ValueError):
        return False

    if num <= 1:
        return False
    for x in range(3, num, 2):  # noqa: SIM110
        if num != 2 and (num % x) == 0:
            return False
    return True


@lru_cache
def is_prime_2(num: int) -> bool:
    """Check if prime."""
    try:
        if isinstance(num, float):
            if not (num == int(num)):
                raise ValueError
        num = int(num)
    except (TypeError, ValueError):
        return False
    if num <= 1:
        return False

    for x in range(2, (num // 2) + 1):  # noqa: SIM110
        if (num % x) == 0:
            return False
    return True


def is_prime_3(num: int) -> bool:
    """Check if prime."""
    try:
        if isinstance(num, float):
            if not (num == int(num)):
                raise ValueError
        num = int(num)
    except (TypeError, ValueError):
        return False
    if num <= 1:
        return False
    return all(num % x != 0 for x in range(2, num // 2 + 1))


@lru_cache
def is_prime_4(num: int) -> bool:
    """Check if prime."""
    try:
        if isinstance(num, float):
            if not (num == int(num)):
                raise ValueError
        num = int(num)
    except (TypeError, ValueError):
        return False
    if num <= 1:
        return False
    return all(num % n != 0 for n in range(2, num // 2 + 1))


@lru_cache
def is_prime(num: int) -> bool:
    """Check if prime."""
    try:
        if isinstance(num, float):
            if not (num == int(num)):
                raise ValueError
        num = int(num)
    except (TypeError, ValueError):
        return False
    if num <= 1:
        return False
    return all(num % n != 0 for n in range(3, int(num**(1/2)) + 1), 2)


def gen_prime():
    """Prime generator."""
    counter = count(1)
    while True:
        if is_prime1(n := next(counter)):
            yield n
