"""dojo module."""

from icecream import ic


class Solutions:
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

    def longest_consecutive1(self, nums: list[int]) -> int:
        """Solution."""
        nums_set = set(nums)
        longest_streak = 0

        for num in nums:
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1
            while current_num + 1 in nums_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(current_streak, longest_streak)

        return longest_streak
