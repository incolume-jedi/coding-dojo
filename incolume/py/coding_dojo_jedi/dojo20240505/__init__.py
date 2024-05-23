"""Module."""

from __future__ import annotations

# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'  # pragma: no cover

from typing import Final, NoReturn


class CPF:
    """CPF class."""

    CPF_DIGITS: Final[int] = 11

    def __init__(self, cpf_number: str | int):
        """Init class."""
        self.__cpf_number: list[int] = []
        self.cpf_number = cpf_number

    @property
    def cpf_number(self) -> str:
        """Return cpf formated."""
        return '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*self.__cpf_number)

    @cpf_number.setter
    def cpf_number(self, value: str | int) -> NoReturn:
        """Check cpf number."""
        cpf = [int(d) for d in str(value) if d.isdigit()]

        if not cpf or len(cpf) < self.CPF_DIGITS or len(set(cpf)) == 1:
            msg = 'Informe 11 digitos numericos distintos.'
            raise ValueError(msg)

        self.__cpf_number = cpf

    def __bool__(self) -> bool:
        """Validade this CPF."""
        novo = self.__cpf_number[:9]
        while len(novo) < self.CPF_DIGITS:
            resto = (
                sum(v * (len(novo) + 1 - i) for i, v in enumerate(novo)) % 11
            )
            digito_verificador = 0 if resto <= 1 else 11 - resto
            novo.append(digito_verificador)
        return self.__cpf_number == novo

    def is_valid(self) -> bool:
        """Validade object."""
        return self.__bool__()

    def __repr__(self) -> str:
        """Repr."""
        return f'{self.__class__.__name__}({self.cpf_number})'

    def __format__(self, format_spec: str) -> str:
        """Output format for object."""
        formats = {
            'r': self.__repr__(),
            's': '{}{}{}{}{}{}{}{}{}{}{}'.format(*self.__cpf_number),
        }
        return formats.get(format_spec, self.__repr__())
