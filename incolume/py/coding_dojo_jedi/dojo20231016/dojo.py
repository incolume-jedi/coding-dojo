# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover


def from_roman(numero_romano: str) -> int:
    """Transforma número romanos em arábicos."""

    romanos = [
        'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'
    ]
    arabicos = [
        1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
    ]
    result = 0
    if numero_romano in romanos:
        return arabicos[romanos.index(numero_romano)]

    for char in numero_romano:
        result += arabicos[romanos.index(char)]
    # MMIX
    # for idx in range(len(numero_romano)):
    #     print(idx, numero_romano[idx], arabicos[romanos.index(numero_romano[idx])])
    #     if arabicos[romanos.index(numero_romano[idx])]) < arabicos[romanos.index(numero_romano[idx+1])]):

    return result


if __name__ == '__main__':    # pragma: no cover
    print(from_roman('MMIX'))
