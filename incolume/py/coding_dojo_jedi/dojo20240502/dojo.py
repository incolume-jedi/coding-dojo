"""Dojo validação de CPF realizado em 02/05/2024."""

import re
from typing import Final

CPF_DIGITS: Final[int] = 11


def check_cpf(cpf: int | str) -> bool:
    """Verificar se CPF é válido.

    Parâmetros:
        cpf (str|int): CPF a ser validado

    Retorno:
        bool:
            - Falso, quando o CPF não possuir o formato 999.999.999-99;
            - Falso, quando o CPF não possuir 11 caracteres numéricos;
            - Falso, quando os dígitos verificadores forem inválidos;
            - Verdadeiro, caso contrário.

    Exemplos:

    >>> check_cpf('529.982.247-25')
    True
    >>> check_cpf('52998224725')
    False
    >>> check_cpf('111.111.111-11')
    False
    """
    cpf = ''.join(re.findall(r'\d', str(cpf)))

    if not cpf or len(cpf) < CPF_DIGITS or len(set(cpf)) == 1:
        return False

    antigo = [int(d) for d in cpf]

    # Gera CPF com novos dígitos verificadores e compara com CPF informado
    novo = antigo[:9]
    while len(novo) < CPF_DIGITS:
        resto = sum(v * (len(novo) + 1 - i) for i, v in enumerate(novo)) % 11

        digito_verificador = 0 if resto <= 1 else 11 - resto

        novo.append(digito_verificador)

    return novo == antigo


def verify_cpf(cpf: int | str) -> bool:
    """Verificar se CPF é válido.

    Parâmetros:
        cpf (str|int): CPF a ser validado

    Retorno:
        bool:
            - Falso, quando o CPF não possuir o formato 999.999.999-99;
            - Falso, quando o CPF não possuir 11 caracteres numéricos;
            - Falso, quando os dígitos verificadores forem inválidos;
            - Verdadeiro, caso contrário.

    Exemplos:

    >>> verify_cpf('529.982.247-25')
    True
    >>> verify_cpf('52998224725')
    False
    >>> verify_cpf('111.111.111-11')
    False
    """
    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in str(cpf) if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if not cpf or len(numbers) < CPF_DIGITS or len(set(numbers)) == 1:
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(
        a * b for a, b in zip(numbers[0:9], range(10, 1, -1), strict=False)
    )
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(
        a * b for a, b in zip(numbers[0:10], range(11, 1, -1), strict=False)
    )
    expected_digit = (sum_of_products * 10 % 11) % 10

    return numbers[10] == expected_digit
