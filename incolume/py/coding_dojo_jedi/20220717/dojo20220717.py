def palindrome(word):
    ispalindrome = False
    word = str(word)
    rword = ''.join(reversed(word))
    if rword == word:
        ispalindrome = True

    return ispalindrome
