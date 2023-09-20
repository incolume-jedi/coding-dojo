"""Dojo 2022-07-20."""


from typing import Union


def calculadora(op: str, x: Union[int, float], y: Union[int, float]) -> float:
    """Calculadora básica."""
    result = 0
    operadores = '+ - * ** / // %'.split()
    if op not in operadores:
        msg = f'Operador inválido. Use: {" ".join(operadores)}'
        raise ValueError(msg)

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        msg = 'x e y devem ser valores numéricos reais.'
        raise ValueError(msg)

    try:
        if op == '+':
            result = x + y
        if op == '-':
            result = x - y
        if op == '*':
            result = x * y
        if op == '/':
            result = x / y
        if op == '%':
            result = x % y
        if op == '//':
            result = x // y
        if op == '**':
            result = x**y
    except ZeroDivisionError:
        msg = 'y deve ser diferente 0.'
        raise ValueError(msg)

    return result
