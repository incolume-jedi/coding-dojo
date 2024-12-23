"""dojo module."""

import itertools
from collections.abc import Container


def dojo(array: Container) -> int:
    """Dojo solution."""
    return list(itertools.permutations(array))
