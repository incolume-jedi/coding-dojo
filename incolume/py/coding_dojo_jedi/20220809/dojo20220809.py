def calculadora(op, x, y):
    """Realiza uma operação matemática.

    :param op: operador (str),
    :param x: valor numérico (float|int|str)
    :param y: valor numérico (float|int|str)
    :return: retorna um valor numérico (float)
    """
    operadores = '+ - * ** // / %'

    if op not in operadores.split():
        msg = f'Operador inválido. Use: {", ".join(operadores.split())}'
        raise ValueError(
            msg,
        )

    if not (isinstance(x, (int, float)) or isinstance(y, (int, float))):
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


if __name__ == '__main__':
    import doctest

    doctest.testfile('tests/calc.txt')
