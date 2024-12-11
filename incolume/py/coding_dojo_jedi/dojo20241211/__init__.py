"""dojo module."""

import secrets
from typing import Final


def gen_cnpj_verify(num: str | int = '') -> str:
    """Generate CNPJ."""
    digitos: Final[int] = 14
    num = num or ''.join(str(secrets.randbelow(10)) for _ in range(13))
    base = [x for x in str(num) if x.isdigit()]

    if len(base) < digitos - 2:
        msg = 'Quantidade insuficiente de números'
        raise ValueError(msg)

    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    result = list(map(int, base))[:12]
    while len(result) < digitos:
        r = sum(x * y for x, y in zip(prod, result, strict=False)) % 11
        f = 11 - r if r > 1 else 0
        result.append(f)
        prod.insert(0, 6)

    return ''.join(map(str, result))


def dojo(*args: str, **kwargs: str) -> dict[str]:
    """Dojo solution."""
    kwargs['args'] = args
    return kwargs
