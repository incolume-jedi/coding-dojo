# !/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Container, List, Set, Tuple

__author__ = '@britodfbr'  # pragma: no cover


def max_sequence(container: (List | Set | Tuple | Container)):
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
