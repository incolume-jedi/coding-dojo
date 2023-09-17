def calculadora(op, x, y):
    operadores = '+ - * ** // / %'.split()

    if op not in operadores:
        msg = f'Operador inválido. Use: {", ".join(operadores)}'
        raise ValueError(msg)

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        msg = 'x e y devem ser valores numéricos reais.'
        raise ValueError(msg)

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
        result = run.get(op)()
    except ZeroDivisionError:
        msg = 'y deve ser diferente de 0'
        raise ValueError(msg)

    return result
