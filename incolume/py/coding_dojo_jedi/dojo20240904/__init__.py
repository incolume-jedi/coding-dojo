"""dojo module."""


def rot47_0(s: str) -> str:
    """Rot47.

    implementação retirada de
    https://rot47.net/#:~:text=The%20ROT47%20(Caesar%20cipher%20by,will%20get%20the%20origin%20text.
    """
    x = []
    for i in range(len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:  # noqa: PLR2004
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)


def rot47_1(s: str) -> str:
    """Rot47."""
    limits = 33, 126
    x = []
    for i in range(len(s)):
        j = ord(s[i])
        if limits[0] <= j <= limits[1]:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)


def rot47(s: str) -> str:
    """Rot47."""
    limits = 33, 126
    result = []
    for char in s:
        j = ord(char)
        if limits[0] <= j <= limits[1]:
            result.append(chr(33 + ((j + 14) % 94)))
        else:
            result.append(char)
    return ''.join(result)
