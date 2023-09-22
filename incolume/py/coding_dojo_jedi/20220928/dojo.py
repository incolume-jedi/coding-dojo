"""Dojo."""
# !/usr/bin/env python
from typing import Iterable

__author__ = '@britodfbr'  # pragma: no cover


def max_sequence(container: Iterable):
    """Localiza a maxima sequência."""
    result = 0
    if not container or all(x < 0 for x in container):
        return result

    for i in container:
        result += i
        if result >= 0:
            ...
        else:
            result = 0

    return result
