import logging
from sys import version_info

if version_info > (3, 7, 15):
    logging.warning("This code running only Python 3.8+")
    exit(0)


def calculadora(op: str, x: (int | float), y: (int | float)) -> float:
    result = 0
    operadores = "+ - * ** / // %".split()
    if op not in operadores:
        raise ValueError(f'Operador inválido. Use: {" ".join(operadores)}')

    try:
        x = float(x)
        y = float(y)
    except:
        raise ValueError("x e y devem ser valores numéricos reais.")

    try:
        if op == "+":
            result = x + y
        if op == "-":
            result = x - y
        if op == "*":
            result = x * y
        if op == "/":
            result = x / y
        if op == "%":
            result = x % y
        if op == "//":
            result = x // y
        if op == "**":
            result = x**y
    except ZeroDivisionError:
        raise ValueError("y deve ser diferente 0.")

    return result
