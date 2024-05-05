"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import annotations

import random
import secrets
from typing import Final

__author__ = '@britodfbr'  # pragma: no cover
CPF_DIGITS: Final[int] = 11


def gen_cpf0() -> str:
    """Gerador de CPF aleatórios."""
    prefix = [random.randint(0, 9) for _ in range(9)]  # noqa: S311

    while len(prefix) < CPF_DIGITS:
        resto = (
            sum(v * (len(prefix) + 1 - i) for i, v in enumerate(prefix)) % 11
        )
        digito_verificador = 0 if resto <= 1 else 11 - resto
        prefix.append(digito_verificador)
    return ''.join(str(n) for n in prefix)


def gen_cpf1() -> str:
    """Gerador de CPF aleatórios."""
    prefix = [int(char) for char in secrets.token_hex(13) if char.isdigit()][
        :9
    ]
    while len(prefix) < CPF_DIGITS:
        resto = (
            sum(v * (len(prefix) + 1 - i) for i, v in enumerate(prefix)) % 11
        )
        digito_verificador = 0 if resto <= 1 else 11 - resto
        prefix.append(digito_verificador)
    return ''.join(str(n) for n in prefix)


def gen_cpf() -> str:
    """Gerador de CPF aleatórios."""
    prefix = [int(char) for char in secrets.token_hex(13) if char.isdigit()][
        :9
    ]

    dig1 = sum(a * b for a, b in zip(prefix, range(10, 1, -1), strict=False))
    prefix.append((dig1 * 10 % 11) % 10)

    dig2 = sum(a * b for a, b in zip(prefix, range(11, 1, -1), strict=False))
    prefix.append((dig2 * 10 % 11) % 10)

    return ''.join(str(n) for n in prefix)
