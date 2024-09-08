"""dojo module."""

from collections import defaultdict


def dojo(nums: list[int]) -> list[int]:
    """Solution dojo."""
    values = defaultdict(int)
    for x in nums:
        values[x] += 1
    result = {key: value for key, value in values.items() if value == 1}
    return result.keys()
