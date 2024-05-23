"""Module."""

from functools import lru_cache
from itertools import chain, count


def is_prime0(num: int) -> bool:
    """Check if prime."""
    if num <= 1:
        return False
    for x in range(2, num):  # noqa: SIM110
        if (num % x) == 0:
            return False
    return True


@lru_cache
def is_prime1(num: int) -> bool:
    """Check if prime."""
    if num <= 1:
        return False

    for x in range(2, (num // 2) + 1):  # noqa: SIM110
        if (num % x) == 0:
            return False
    return True


def is_prime(num: int) -> bool:
    """Check if prime."""
    if num <= 1:
        return False
    return all(num % x != 0 for x in range(2, num // 2 + 1))


def gen_prime():
    """Prime generator."""
    counter = count(1)
    while True:
        if is_prime1(n := next(counter)):
            yield n


def merge_matrix0(*args: list[int]) -> list:
    """merge_matrix."""
    a = []
    for array in args:
        a += array
    return list(set(a))


def merge_matrix(*args: list[int]) -> list:
    """merge_matrix."""
    return list(set(chain.from_iterable(args)))
