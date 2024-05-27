"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'  # pragma: no cover


def soma_pythonic(num: int) -> int:
    """Somo algarismo do numero."""
    return sum(int(n) for n in str(num))


def soma0(num: int) -> int:
    """Somo algarismo do numero."""
    numbers = []
    while num > 0:
        numbers.append(num % 10)
        num //= 10
    return sum(numbers)


def soma(num: int) -> int:
    """Somo algarismo do numero."""
    result = 0
    while num > 0:
        result += num % 10
        num //= 10
    return result
