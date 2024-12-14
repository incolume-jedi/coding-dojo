"""dojo module."""

from icecream import ic


class Solution:
    """Solution."""

    def longest_consecutive(self, nums: list[int]) -> int:
        """Dojo solution."""
        result, temp = 1, 1
        nums.sort()
        ic(nums)
        for idx, x in enumerate(nums):
            ic(idx, x)
            if x + 1 in nums and nums[idx + 1] == x + 1:
                temp += 1
                ic(temp)
            elif temp > result:
                ic(result)
                result, temp = temp, 1
                ic(result)
        return result
