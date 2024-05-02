"""Dojo."""


def index0(pos: int) -> str:
    """Problema 1."""
    s = 'Python'
    ss = ''
    for _ in range(pos + 1):
        ss += s
    return ss[pos]


def index1(pos: int) -> str:
    """Problema 1."""
    s = 'Python'
    return s[pos % len(s)]


def index(palavra: str, pos: int) -> str:
    """Problema 2."""
    return palavra[pos % len(palavra)]


def adedonha(num: int) -> str:
    """Contagem de letras com regras de adedonha."""
    alfabeto = 'abcdefghijklmnopqrstuvxwyz'
    return alfabeto[num % len(alfabeto) - 1]


if __name__ == '__main__':
    print(
        index(input('Qual a palavra: '), int(input('Qual a posição: '))),
    )
