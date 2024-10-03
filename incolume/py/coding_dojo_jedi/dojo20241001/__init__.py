"""dojo module."""


def dojo(dictmap: dict[str]) -> str:
    """Dojo solution."""
    length = len([item for items in dictmap.values() for item in items])
    result = ['' for _ in range(length)]
    for letter, positions in dictmap.items():
        for pos in positions:
            result[pos] = letter
    return ''.join(result)
