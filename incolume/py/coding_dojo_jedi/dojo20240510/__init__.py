"""Module."""

import logging

# !/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict
from functools import lru_cache

__author__ = '@britodfbr'  # pragma: no cover

from collections.abc import Container


@lru_cache
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


def counting_sheep0(array: list) -> int:
    """Count sheeps."""
    if isinstance(array[0], Container):
        array = [item for m in array for item in m]
    for i, item in enumerate(array):
        if not isinstance(item, bool) and item != 'True':
            array[i] = False
    return sum(array)


def counting_sheep(array: list) -> int:
    """Count sheeps."""
    if isinstance(array[0], Container):
        array = [item for m in array for item in m]
    for i, item in enumerate([str(m) for m in array]):
        array[i] = item.casefold() == 'true'
    logging.debug(array)
    return sum(array)
