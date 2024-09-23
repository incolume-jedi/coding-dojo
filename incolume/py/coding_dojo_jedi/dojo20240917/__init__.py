"""dojo module."""

from typing import NoReturn


def is_palindrome(string, low, high):
    """Function to check if a substring s[low..high] is a palindrome."""
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True


def validate(string: str) -> NoReturn:
    """VAlidadte."""
    ascii_values = (32, 127)
    n = len(string)
    msg = ''
    if any(
        x
        for x in string
        if ascii_values[0] > ord(x) or ord(x) > ascii_values[-1]
    ):
        msg = 'Not ASCII characters.'
        raise UnicodeError(msg)

    if n > 1000:  # noqa: PLR2004
        msg = 'Limit until 1000 characters.'
        raise ValueError(msg)


def dojo(string: str) -> str:
    """This function prints the longest palindrome substring.

    It also returns the length of the longest palindrome
    """
    n = len(string)

    validate(string=string)

    # All substrings of length 1 are palindromes
    max_len = 1
    start = 0

    # Nested loop to mark start and end index
    for i in range(n):
        for j in range(i, n):
            # Check if the current substring is
            # a palindrome
            if is_palindrome(string, i, j) and (j - i + 1) > max_len:
                start = i
                max_len = j - i + 1

    return result if len(result := string[start : start + max_len]) > 1 else ''
