"""dojo module."""

import logging


def is_even(num: int) -> bool:
    """Verify is even."""
    return not num % 2


def last_digit_for_pow5_0(expoente: int) -> int:
    """Ultimo digito para potencia de 5."""
    return 5**expoente % 10


def last_digit_for_pow5(expoente: int) -> int:
    """Ultimo digito para potencia de 5."""
    return 0 if is_even(expoente) else 5


def last_digit_for_pow7_0(expoente: int) -> int:
    """Ultimo digito para potencia de 7."""
    return 7**expoente % 10


def last_digit_for_pow7(expoente: int) -> int:
    """Ultimo digito para potencia de 7."""
    freq = 4
    possible = [7**x % 10 for x in range(1, freq + 1)]
    logging.debug(expoente, possible)
    return possible[(expoente % freq) - 1]
