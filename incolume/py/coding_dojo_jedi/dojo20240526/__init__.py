"""Module."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from collections.abc import Generator
from functools import lru_cache
from itertools import count

__author__ = '@britodfbr'  # pragma: no cover


@lru_cache
def is_palindrome(num: int) -> bool:
    """Check if palindrome."""
    return str(num) == str(num)[::-1]


@lru_cache
def is_prime(num: int) -> bool:
    """Check if prime."""
    if num <= 1:
        return False
    return all(num % n != 0 for n in range(2, num // 2 + 1))


@lru_cache
def is_palindrome_prime(num: int) -> bool:
    """Check if palindrome and prime."""
    return is_palindrome(num) and is_prime(num)


def gen_palindrome_prime() -> Generator:
    """Generator for numbers palindrome and prime."""
    c = count(2)
    while 1:
        if is_prime(n := next(c)) and is_palindrome_prime(n):
            yield n
