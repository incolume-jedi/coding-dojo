"""Dojo."""


def square(num: int):
    """Retorna área de quadrado."""
    if num < 0:
        return False
    result = num ** (1 / 2)
    return result == int(result)
