"""Dojo."""

import logging


def no_exclamation0(frase: str) -> str:
    """Problema 1."""
    result = ''
    for letra in frase:
        if letra != '!':
            result += letra
    return result


def no_exclamation1(frase: str) -> str:
    """Problema 1."""
    return ''.join(x for x in frase if x != '!')


def no_exclamation(frase: str) -> str:
    """Problema 1."""
    return frase.replace('!', '')


def tabuada(tab_ref: int, inicial: int = 1, final: int = 10) -> list:
    """Problema 2."""
    result = []
    inicial, final = min(inicial, final), max(inicial, final)
    for x in range(inicial, final + 1):
        s = f'{tab_ref} X {x} = {tab_ref * x}'
        result.append(s)
    return result


def imc0(altura: float, peso: float) -> str:
    """Problema 3."""
    imc_value = peso / altura**2
    return [
        'Obesidade III',
        'Obesidade II',
        'Obesidade I',
        'Sobrepeso',
        'peso normal',
        'abaixo do peso',
    ][
        (imc_value < 39.9)
        + (imc_value < 34.9)
        + (imc_value < 29.9)
        + (imc_value < 24.9)
        + (imc_value < 18.5)
    ]


def imc(altura: float, peso: float) -> str:
    """Problema 3."""
    imc_value = peso / altura**2
    mark = {
        'Obesidade III': 40.0,
        'Obesidade II': 39.9,
        'Obesidade I': 34.9,
        'Sobrepeso': 29.9,
        'peso normal': 24.9,
        'abaixo do peso': 18.5,
    }
    logging.debug(m := list(mark.keys()))
    return m[
        (imc_value < mark['Obesidade II'])
        + (imc_value < mark['Obesidade I'])
        + (imc_value < mark['Sobrepeso'])
        + (imc_value < mark['peso normal'])
        + (imc_value < mark['abaixo do peso'])
    ]
