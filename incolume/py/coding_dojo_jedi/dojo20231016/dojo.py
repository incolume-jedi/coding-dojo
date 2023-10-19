"""dojo 20231016."""
# !/usr/bin/env python
__author__ = '@britodfbr'  # pragma: no cover

romanos = [
    'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I',
]
arabicos = [
    1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1,
]


def from_roman0(numero_romano: str) -> int:
    """Transforma número romanos em arábicos."""
    result = 0
    if numero_romano in romanos:
        return arabicos[romanos.index(numero_romano)]
    for char in numero_romano:
        result += arabicos[romanos.index(char)]
    return result


def from_roman(numero_romano: str) -> int:
    """Transforma número romanos em arábicos."""
    # MMIX
    result = 0
    qnt = len(numero_romano)
    for idx in range(qnt):
        if (
            idx + 1 < qnt and (
                arabicos[romanos.index(numero_romano[idx])] <
                arabicos[romanos.index(numero_romano[idx + 1])]
            )
        ):
            result -= arabicos[romanos.index(numero_romano[idx])]
        else:
            result += arabicos[romanos.index(numero_romano[idx])]

    return result
