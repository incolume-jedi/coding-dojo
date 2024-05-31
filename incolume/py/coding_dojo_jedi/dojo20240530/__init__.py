"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import re

__author__ = '@britodfbr'  # pragma: no cover

from typing import Final


def validar_cnpj(cnpj: str) -> bool:
    """Valida CNPJs, retornando True para números válida.

    :: Examples:

    # CNPJs errados
    >>> validar_cnpj('abcdefghijklmn')
    False
    >>> validar_cnpj('123')
    False
    >>> validar_cnpj('')
    False
    >>> validar_cnpj(None)
    False
    >>> validar_cnpj('12345678901234')
    False
    >>> validar_cnpj('11222333000100')
    False

    # CNPJs corretos
    >>> validar_cnpj(11222333000181)
    True
    >>> validar_cnpj('11222333000181')
    True
    >>> validar_cnpj('11.222.333/0001-81')
    True
    >>> validar_cnpj('  11 222 333 0001 81  ')
    True
    """
    digitos: Final[int] = 14
    cnpj = ''.join(re.findall(r'\d', str(cnpj)))

    if (not cnpj) or (len(cnpj) < digitos):
        return False
    # Pega apenas os 12 primeiros dígitos do CNPJ
    # e gera os 2 dígitos que faltam
    inteiros = list(map(int, cnpj))
    novo = inteiros[:12]

    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    while len(novo) < digitos:
        r = sum(x * y for x, y in zip(novo, prod, strict=False)) % 11
        f = 11 - r if r > 1 else 0
        novo.append(f)
        prod.insert(0, 6)

    # Se o número gerado coincidir com o número original, é válido
    return novo == inteiros
