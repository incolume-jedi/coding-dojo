"""dojo module."""


def dojo(dictmap: dict[str]) -> str:
    """Dojo solution."""
    result = []
    for idx, (letter, positions) in enumerate(dictmap.items()):
        print(letter, positions)
        for position in positions:
            if position == idx:
                result.append(letter)
    return result
