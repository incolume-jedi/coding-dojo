def calculadora(op, x, y):
    operadores = '+ - * ** // / %'.split()

    if op not in operadores:
        raise ValueError(f'Operador inválido. Use: {", ".join(operadores)}')

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        raise ValueError('x e y devem ser valores numéricos reais.')

    run = {
        '+': lambda: x + y,
        '-': lambda: x - y,
        '/': lambda: x / y,
        '//': lambda: x // y,
        '%': lambda: x % y,
        '*': lambda: x * y,
        '**': lambda: x ** y,
    }
    try:
        result = run.get(op)()
    except ZeroDivisionError:
        raise ValueError('y deve ser diferente de 0')

    return result
