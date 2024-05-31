"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'  # pragma: no cover

import logging
import os

from icecream import ic

ic.disable()
if os.getenv('DEBUG_MODE'):
    ic.enable()


def last_dig0(base: int, expoente: int) -> int:
    """Retorna o ultimo digito de uma potência."""
    result = base**expoente
    return result % 10


def last_dig1(base: int, expoente: int) -> int:
    """Retorna o ultimo digito de uma potência."""
    logging.debug(base, expoente)
    result = [int(x) for x in '2486']
    return result[expoente % len(result) - 1]


def last_dig(base: int, expoente: int) -> int:
    """Retorna o ultimo digito de uma potência."""
    result = [int(x) for x in {(base**i) % 10 for i in range(1, 5)}]
    result.sort()
    return result[expoente % len(result)]


def num_extense(num: str) -> int:
    """Recebe numero por extenso e retorna arabico."""
    numbers = {
        'zero': 0,
        'um': 1,
        'dois': 2,
        'três': 3,
        'qutro': 4,
        'cinco': 5,
        'seis': 6,
        'sete': 7,
        'oito': 8,
        'nove': 9,
        'dez': 10,
        'onze': 11,
        'doze': 12,
        'treze': 13,
        'catorze': 14,
        'quize': 15,
        'dezesseis': 16,
        'dezessete': 17,
        'dezoito': 18,
        'dezenove': 19,
        'vinte': 20,
        'trinta': 30,
        'quarenta': 40,
        'cinquenta': 50,
        'sessenta': 60,
        'setenta': 70,
        'oitenta': 80,
        'noventa': 90,
        'cem': 100,
        'cento': 100,
        'duzentos': 200,
        'trezentos': 300,
        'quatrocentos': 400,
        'quinhentos': 500,
        'seiscentos': 600,
        'setecentos': 700,
        'oitocentos': 800,
        'novecentos': 900,
        'mil': 1000,
    }
    array = num.replace(' e ', ' ').split()
    return ic(sum(numbers.get(ic(x)) for x in array))
