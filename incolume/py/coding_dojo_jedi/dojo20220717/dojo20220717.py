"""Dojo."""


def palindrome(word: str) -> bool:
    """Return if is palindrome."""
    ispalindrome = False
    word = str(word)
    rword = ''.join(reversed(word))
    if rword == word:
        ispalindrome = True

    return ispalindrome
