"""Dojo."""

import inspect
import logging
from typing import Final

MOEDAS: Final = [1.00, 0.5, 0.25, 0.10, 0.05, 0.01]
CEDULAS: Final = [200, 100, 50, 20, 10, 5, 2]

logging.basicConfig(level=logging.DEBUG)


def calcular(valor: float, base_monetaria: list) -> tuple:
    """Calculadora de notas."""
    logging.debug('%s(%s, %s)', inspect.stack()[0][3], valor, base_monetaria)
    result = [0] * len(base_monetaria)
    for i, base in enumerate(base_monetaria):
        result[i] = int(valor / base)
        valor = round(valor % base, 2)
        logging.debug('%s %s %s', valor, result[i], base)
    logging.debug('%s, %s', valor, result)
    return valor, result


def trocar_dinheiro(valor: float) -> tuple[list, list]:
    """Calcula o menor número de notas e moedas possíveis."""
    valor, cedulas = calcular(valor, CEDULAS)
    valor, moedas = calcular(valor, MOEDAS)
    # if valor:
    return (
        cedulas,
        moedas,
    )


if __name__ == '__main__':  # pragma: no cover
    trocar_dinheiro(386.96)
    trocar_dinheiro(576.73)
    trocar_dinheiro(6)
