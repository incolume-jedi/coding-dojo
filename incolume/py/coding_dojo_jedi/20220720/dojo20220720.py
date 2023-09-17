from typing import Union


def calculadora(op: str, x: Union[int, float], y: Union[int, float]) -> float:
    result = 0
    operadores = '+ - * ** / // %'.split()
    if op not in operadores:
        raise ValueError(f'Operador inválido. Use: {" ".join(operadores)}')

    try:
        x = float(x)
        y = float(y)
    except:
        raise ValueError('x e y devem ser valores numéricos reais.')

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
        raise ValueError('y deve ser diferente 0.')

    return result
