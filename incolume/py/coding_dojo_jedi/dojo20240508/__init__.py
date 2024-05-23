"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass
from functools import lru_cache
from itertools import count

from incolume.py.coding_dojo_jedi.dojo20240507 import is_feliz

__author__ = '@britodfbr'  # pragma: no cover


def double_minor_feliz():
    """Felizes consecutivos."""
    num = count(1)
    while True:
        n = next(num)
        if is_feliz(n) and is_feliz(n + 1):
            return n, n + 1


def trio_minor_feliz():
    """Felizes consecutivos."""
    num = count(1)
    while True:
        n = next(num)
        if is_feliz(n) and is_feliz(n + 1) and is_feliz(n + 2):
            return n, n + 1, n + 2


def alt_num_feliz(num: int) -> int:
    """Altura de número feliz.

    return: -1 para não felizes.
    """
    for altura, _ in enumerate(range(pow(10, 5)), start=1):
        n = [pow(int(n), 2) for n in str(num)]
        if (snum := sum(n)) == 1:
            return altura
        num = snum

    return -1


__height = 0


@lru_cache
def isfeliz(num: int) -> bool:
    """Verifica se numero é feliz."""
    global __height  # noqa: PLW0603
    __height += 1
    num = [pow(int(n), 2) for n in str(num)]

    if (snum := sum(num)) == 1:
        return True, __height

    try:
        return is_feliz(snum), __height
    except RecursionError:
        return False


@dataclass
class NFeliz:
    """NFeliz class."""

    num: int
    __height: int = 0
    __is_feliz: bool | None = None

    @property
    def height(self):
        """Height."""
        return self.__height

    def __post_init__(self):
        """Post init."""
        self.__is_feliz, self.__height = isfeliz(self.num)

    def __bool__(self):
        """Self bool."""
        return self.__is_feliz
