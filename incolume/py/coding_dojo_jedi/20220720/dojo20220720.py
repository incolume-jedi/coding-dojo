"""Dojo 2022-07-20."""


def calculadora(op: str, x: float, y: float) -> float:
    """Calculadora básica."""
    result: float = 0
    operadores = '+ - * ** / // %'.split()
    if op not in operadores:
        msg = f'Operador inválido. Use: {" ".join(operadores)}'
        raise ValueError(msg)

    try:
        x = float(x)
        y = float(y)
    except (ValueError, TypeError) as err:
        msg = 'x e y devem ser valores numéricos reais.'
        raise TypeError(msg) from err

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
    except ZeroDivisionError as err:
        msg = 'y deve ser diferente 0.'
        raise ValueError(msg) from err

    return result
