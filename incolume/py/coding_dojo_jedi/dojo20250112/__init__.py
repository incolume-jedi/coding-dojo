"""dojo module."""

from __future__ import annotations

from functools import lru_cache
from itertools import count
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator


def is_prime_0(num: int | bytes | str) -> bool:
    """Check if prime."""
    try:
        tnum = int(num)
        if (isinstance(num, float) and num != tnum) or tnum <= 1:
            return False
    except (TypeError, ValueError):
        return False

    for x in range(2, tnum):  # noqa: SIM110
        if (tnum % x) == 0:
            return False
    return True


def is_prime_1(num: int | bytes | str) -> bool:
    """Check if prime."""
    try:
        if isinstance(num, float) or num != int(num):
            return False
        num = int(num)
    except (TypeError, ValueError):
        return False

    if num <= 1 or (num > 2 and num % 2 == 0):
        return False
    for x in range(3, num, 2):  # noqa: SIM110
        if (num % x) == 0:
            return False
    return True


@lru_cache
def is_prime_2(num: int) -> bool:
    """Check if prime."""
    try:
        if isinstance(num, float) or num != int(num):
            return False
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
        if isinstance(num, float) or num != int(num):
            return False
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
        if isinstance(num, float) and num != int(num):
            return False
        num = int(num)
    except (TypeError, ValueError):
        return False
    if num <= 1:
        return False
    return all(num % n != 0 for n in range(2, num // 2 + 1))


@lru_cache
def is_prime_5(num: int) -> bool:
    """Check if prime number."""
    try:
        if isinstance(num, float) and num != int(num):
            return False
        num = int(num)
    except (TypeError, ValueError):
        return False
    if num <= 1 or (num > 2 and num % 2 == 0):  # noqa: PLR2004
        return False
    return all(num % n != 0 for n in range(2, num // 2 + 1))


@lru_cache
def is_prime(num: str | bytes | float) -> bool:
    """Check if prime number."""
    try:
        if isinstance(num, float) and num != int(num):
            return False
        num = int(num)
    except (TypeError, ValueError):
        return False

    if num <= 1 or (num > 2 and num % 2 == 0):  # noqa: PLR2004
        return False
    return all(num % n != 0 for n in range(3, int(num**0.5) + 1, 2))


def gen_prime(initial: int = 2) -> Generator:
    """Prime generator."""
    initial = max(2, initial) or 2
    counter = count(initial)
    while True:
        if is_prime(n := next(counter)):
            yield n
