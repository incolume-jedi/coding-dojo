"""dojo module."""

from collections.abc import Container
from itertools import chain, combinations


def dojo(array: Container) -> int:
    """Dojo solution."""
    return sum(
        chain.from_iterable([
            min(combinations(array, x + 1)) for x in range(len(array))
        ]),
    )


def sum_subarray_mins(array: list[int]) -> int:
    """Python program to return required minimum sum."""
    # To store answer
    ans = 0
    n = len(array)
    for i in range(n):
        # To store minimum element
        min_ele = array[i]
        for j in range(i, n):
            # Finding minimum element of subarray
            min_ele = min(min_ele, array[j])
            # Adding that minimum element of subarray to answer
            ans += min_ele
    return ans
