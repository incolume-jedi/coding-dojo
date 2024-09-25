"""dojo module."""

from dataclasses import dataclass


class SizeError(Exception):
    """Size error."""


@dataclass
class Rules:
    """Rules."""


def is_validate(value: list) -> bool:
    """Validade entrance."""
    rules = Rules()
    rules.max_value = 100
    rules.max_size = 30
    rules.merr_value = f'Somente valores entre 0 e {rules.max_value}'
    rules.merr_sz = f'Quantidade maxima de nodos é {rules.max_size}'

    if len(value) > rules.max_size:
        raise SizeError(rules.merr_sz)

    if any(x for x in value if x > rules.max_value or x < 0):
        raise ValueError(rules.merr_value)

    return bool(value)


def dojo(lista: list, nodo: int) -> list[int]:
    """Dojo solution."""
    is_validate(lista)
    try:
        lista.pop(nodo)
    except IndexError:
        lista.pop(-1)
    return lista
