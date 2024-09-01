"""dojo module."""

from collections import defaultdict


def dojo(nums: list[int], target: int) -> list[int]:
    """Answer for dojo."""
    hashmap = defaultdict(int)
    for idx, num in enumerate(nums):
        difference = target - num
        if difference in hashmap:
            return [hashmap[difference], idx]
        hashmap[num] = idx
    return hashmap
