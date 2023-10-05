"""Dojo."""


def to_roman0(num: int) -> str:
    """Convert arabics to romans."""
    nums = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }
    result = ''
    # pylint: disable=consider-using-dict-items
    for i in nums:
        while num >= i:
            num = num - i
            result = result + nums[i]
    return result


def to_roman1(num: int) -> str:
    """Convert arabics to romans."""
    nums = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }
    result = ''
    # pylint: disable=consider-using-dict-items
    for i in nums:
        while num >= i:
            num -= i
            result += nums[i]
    # pylint: enable=consider-using-dict-items
    return result


def to_roman(num: int) -> str:
    """Convert arabics to romans."""
    nums = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }
    result = ''
    for i, value in nums.items():
        while num >= i:
            num -= i
            result += value
    return result
