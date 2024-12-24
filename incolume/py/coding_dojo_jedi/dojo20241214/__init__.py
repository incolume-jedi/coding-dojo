"""dojo module."""

from collections import Counter

from icecream import ic


class Solutions:
    """Solutions."""

    def dojo2(self, nums: list[int], k: int = 1) -> list[int]:
        """Dojo solution."""
        result = {(x, nums.count(x)) for x in nums}
        result = [
            a[0]
            for a in sorted(
                result,
                key=lambda x: x[1],
                reverse=True,
            )
        ]
        ic(result)
        return result[:k]

    def dojo1(self, nums: list[int], k: int = 1) -> list[int]:
        """Dojo solution."""
        check = {x: nums.count(x) for x in nums}
        result = sorted(check.items(), key=lambda x: x[1], reverse=True)
        result = [x for x, _ in result][:k]
        ic(result)
        return result

    def dojo(self, nums: list[int], k: int = 1) -> list[int]:
        """Dojo solution."""
        check = {x: nums.count(x) for x in nums}
        result = [x for x, _ in Counter(check).most_common(k)]
        ic(result)
        return result
