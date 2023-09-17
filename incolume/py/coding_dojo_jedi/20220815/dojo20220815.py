def index0(pos: int) -> str:
    """Problema 1."""
    s = 'Python'
    ss = ''
    for i in range(pos + 1):
        ss += s
    return ss[pos]


def index1(pos: int) -> str:
    """Problema 1."""
    s = 'Python'
    return s[pos % len(s)]


def index(palavra: str, pos: int) -> str:
    """problema 2."""
    return palavra[pos % len(palavra)]


def adedonha(num: int) -> str:
    alfabeto = 'abcdefghijklmnopqrstuvxwyz'
    return alfabeto[num % len(alfabeto) - 1]


if __name__ == '__main__':
    print(index(input('Qual a palavra: '), int(input('Qual a posição: '))))
