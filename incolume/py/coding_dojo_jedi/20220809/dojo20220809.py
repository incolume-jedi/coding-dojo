def calculadora(op, x, y):
    """Realiza uma operação matemática.

    :param op: operador (str),
    :param x: valor numérico (float|int|str)
    :param y: valor numérico (float|int|str)
    :return: retorna um valor numérico (float)
    """
    operadores = '+ - * ** // / %'

    if op not in operadores.split():
        raise ValueError(
            f'Operador inválido. Use: {", ".join(operadores.split())}'
        )

    if not (isinstance(x, (int, float)) or isinstance(y, (int, float))):
        raise ValueError('x e y devem ser valores numéricos reais.')

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
        raise ValueError('y deve ser diferente de 0')
    return result


if __name__ == '__main__':
    import doctest

    doctest.testfile('tests/calc.txt')
