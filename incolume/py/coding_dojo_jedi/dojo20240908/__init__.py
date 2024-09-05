"""dojo module."""


def is_even(num: int) -> bool:
    """Verify is even."""
    return not num % 2


def last_digit_for_pow5(expoente: int) -> int:
    """Ultimo digito para potencia de 5."""
    return 0 if is_even(expoente) else 5
