"""Module."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import cycle
from random import shuffle

__author__ = '@britodfbr'  # pragma: no cover

from collections.abc import Container, Generator


def gen_playlist(array: Container) -> Generator:
    """Playlist."""
    array = list(array)
    shuffle(array)
    while True:
        last = array.pop(0)
        array.append(last)
        yield last


def playlist(lst: Container) -> Generator:
    """Playlist."""
    lst = list(lst)
    shuffle(lst)
    return cycle(lst)
