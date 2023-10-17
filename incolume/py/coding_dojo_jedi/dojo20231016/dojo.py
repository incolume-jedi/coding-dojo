# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover


def from_roman(numero_romano: str) -> int:
    """Transforma número romanos em arábicos."""

    romanos = ["I","V","X","L","C","D","M"]
    arabicos = [1,5,10,50,100,500,1000]
    result = arabicos[romanos.index(numero_romano)]
    return result
