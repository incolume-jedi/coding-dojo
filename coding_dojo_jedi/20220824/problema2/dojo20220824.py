def millisseconds(*, h: int = 0, m: int = 0, s: int = 0) -> int:
    if not (0 <= h <= 23):
        raise ValueError('0 <= h <= 23')

    if not(0 <= m < 60):
        raise ValueError('0 <= m <= 59')

    if not(0 <= s < 60):
        raise ValueError('0 <= s <= 59')

    return (h * 3600 + m * 60 + s) * 1000
