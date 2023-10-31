"""Dojo."""


def is_square(num: int) -> bool:
    """Retorna se a área de quadrado."""
    if num < 0:
        return False
    result = num ** (1 / 2)
    return result == int(result)
