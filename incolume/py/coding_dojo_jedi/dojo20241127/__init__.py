"""dojo module."""

from typing import Final


def dojo(cnpj: str | int) -> int:
    """Dojo solution."""
    digitos: Final[int] = 14

    base = ''.join(x for x in str(cnpj) if x.isdigit())
    if not cnpj or (len(base) < digitos - 2):
        msg = 'Quantidade insuficiente de números'
        raise ValueError(msg)

    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    result = list(map(int, base))[:12]
    while len(result) < digitos:
        r = sum(x * y for x, y in zip(prod, result, strict=False)) % 11
        f = 11 - r if r > 1 else 0
        result.append(f)
        prod.insert(0, 6)

    return int(''.join(map(str, result[-2:])))
