"""dojo module."""

import logging


def dojo(base: int, expoente: int) -> int:
    """Solution."""
    return (base**expoente) % 10


def dojo_0(base: int, expoente: int) -> int:
    """Solution."""
    possible = [(base * x) % 10 for x in range(1, 11)]
    result = possible[expoente % len(possible)]

    logging.debug(result)
    return result
