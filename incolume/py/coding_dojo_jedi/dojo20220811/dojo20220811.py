"""Dojo."""

from typing import Any


def calculadora(op: str, x: Any, y: Any) -> float:
    """Calculadora."""
    operadores = '+ - * ** // / %'.split()

    if op not in operadores:
        msg = f'Operador inválido. Use: {", ".join(operadores)}'
        raise ValueError(msg)

    try:
        x = float(x)
        y = float(y)
    except ValueError as err:
        msg = 'x e y devem ser valores numéricos reais.'
        raise ValueError(msg) from err

    run = {
        '+': lambda: x + y,
        '-': lambda: x - y,
        '/': lambda: x / y,
        '//': lambda: x // y,
        '%': lambda: x % y,
        '*': lambda: x * y,
        '**': lambda: x**y,
    }
    try:
        result = run.get(op, lambda: x + y)()
    except ZeroDivisionError as err:
        msg = 'y deve ser diferente de 0'
        raise ValueError(msg) from err

    return result
