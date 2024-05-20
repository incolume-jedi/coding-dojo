"""Module."""

from functools import lru_cache


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
