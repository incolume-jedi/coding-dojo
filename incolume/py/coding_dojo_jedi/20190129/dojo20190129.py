"""# Problema: Notas e Moedas.

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1021
"""
from typing import Any, Final, List, Tuple, Union

MOEDAS: Final = [1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
NOTAS: Final = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0]


def moedas(valor: float) -> Tuple[List[float], List[float]]:
    """Contabiliza a quantidade de notas e moedas."""
    vnotas: List[float] = [0, 0, 0, 0, 0, 0]
    vmoedas: List[float] = [0, 0, 0, 0, 0, 0]

    valor = calcular(NOTAS, vnotas, valor)
    valor = calcular(MOEDAS, vmoedas, valor)

    return vnotas, vmoedas


def calcular(monetario: float, lista_resutado: list, valor: float) -> float:
    """Fatora o valor de acordo com a base monetária fornecida."""
    for i, moeda in enumerate(monetario):
        while valor >= moeda:
            lista_resutado[i] += 1
            valor -= moeda
            valor = round(valor, 2)
    return valor


# A solução abaixo demonstra alguns dos conceitos que
# comentamos no final do dojo e foi adicionada para fins
# didáticos sobre python


def moedas2(valor: float) -> Tuple[List[float], List[float]]:
    """Contabiliza a quantidade de notas e moedas."""
    (vnotas, valor) = calcula2(valor, NOTAS)
    (vmoedas, valor) = calcula2(valor, MOEDAS)

    return vnotas, vmoedas


def calcula2(
    valor: float,
    cedulas: list,
) -> Tuple[List[int], Union[float, Any]]:
    """Fatora o valor de acordo com a base monetária fornecida."""
    quantidades = [0] * len(cedulas)
    for (i, cedula) in enumerate(cedulas):
        # poderíamos usar divmod() também
        quantidades[i] = int(valor / cedula)
        valor = round(valor % cedula, 2)
    return quantidades, valor
