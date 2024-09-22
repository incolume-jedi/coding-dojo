"""dojo module."""


def v_dac(c: float) -> float:
    """Conversor digital analógico."""
    v = 1023
    ref = 5.0
    return round(c * ref / v, 2)
