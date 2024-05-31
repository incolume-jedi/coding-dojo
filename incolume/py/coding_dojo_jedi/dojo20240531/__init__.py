"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'  # pragma: no cover

import logging


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
