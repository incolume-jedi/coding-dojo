"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Final

__author__ = '@britodfbr'  # pragma: no cover
CPF_DIGITS: Final[int] = 11


def create_cpf(nums: str | int) -> str:
    """Cria digitos verificadores de um CPF válido."""
    cpf = [int(x) for x in str(nums) if x.isdigit()]

    if not cpf or len(cpf) < CPF_DIGITS - 2 or len(set(cpf)) == 1:
        msg = (
            'O número de entrada deve conter 9 digitos,'
            ' com ao menos 1 diferente.'
        )
        raise ValueError(msg)

    while len(cpf) < CPF_DIGITS:
        resto = sum(v * (len(cpf) + 1 - i) for i, v in enumerate(cpf)) % 11
        digito_verificador = 0 if resto <= 1 else 11 - resto
        cpf.append(digito_verificador)

    return '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*cpf)
