"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
from collections.abc import Container
from typing import TypeVar

T = TypeVar('T')


def all_permutations(array: Container[T]) -> list[tuple[T]]:
    """All permutations."""
    return list(itertools.permutations(array))
