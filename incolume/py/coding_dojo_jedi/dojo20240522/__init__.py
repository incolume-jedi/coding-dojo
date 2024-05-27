"""Dojo module."""


def is_palindrome(x: int, limits: tuple = (-231, 232)) -> bool:
    """Check is_palindrome."""
    if x < limits[0] or x > limits[1]:
        msg = f'limited : {limits[0]} <= x <= {limits[1]}'
        raise ValueError(msg)

    return str(x)[::-1] == str(x)
