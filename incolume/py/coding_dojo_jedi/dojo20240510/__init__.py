"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

__author__ = '@britodfbr'  # pragma: no cover


def is_narcisist(num: int) -> bool:
    """Check if number is narcisist number."""
    result = sum(pow(int(n), len(str(num))) for n in str(num) if n.isdigit())
    return num == result


def char_position(text: str) -> dict[str, list[int]]:
    """Mapeia os caracteres de uma string."""
    result = defaultdict(list)
    for i, char in enumerate(text):
        result[char].append(i)
    return result
