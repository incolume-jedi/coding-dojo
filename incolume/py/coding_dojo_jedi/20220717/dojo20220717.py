"""Dojo."""


def palindrome(word):
    """Return if is palindrome."""
    ispalindrome = False
    word = str(word)
    rword = ''.join(reversed(word))
    if rword == word:
        ispalindrome = True

    return ispalindrome
