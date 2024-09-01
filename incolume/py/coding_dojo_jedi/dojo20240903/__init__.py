"""dojo module."""

import logging


def dojo(l1: list[int], l2: list[int]) -> list[int]:
    """Implementation for solution."""
    result = int(''.join(str(x) for x in l1[::-1])) + int(
        ''.join(str(x) for x in l2[::-1]),
    )
    logging.debug(result)
    return [int(x) for x in str(result)[::-1]]
