# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover

from datetime import datetime
from functools import singledispatch


@singledispatch
def validar_entrada(entrance:str):
    """Validar entrada."""
    result = int(entrance)
    return result

@validar_entrada.register(datetime)
def _(entrance: datetime):
    """Validar entrada datetime."""
    return entrance


def milissegundos(*args):
    """Milissegundos."""
    return 0

# def _(*args):
#     """"""
#     h, m, s = validar_entrada(*args)
#     return (h * 3600 + m * 60 + s) * 1000
