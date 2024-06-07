"""dojo module."""


def house_robber(houses: list) -> int:
    """House robber."""
    length: tuple = 1, 100
    val: tuple = 0, 400

    if not houses or min(length) > len(houses) > max(length):
        msg = '1 <= nums.length <= 100'
        raise IndexError(msg)

    if any(not (min(val) <= x <= max(val)) for x in houses):
        msg = '0 <= nums[i] <= 400'
        raise ValueError(msg)

    return max(sum(houses[::2]), sum(houses[1::2]))
