"""Dojo."""


from pprint import pprint


def tower0(n_floors: int, char: str | None = None) -> list:
    """Construção de piramide ascii."""
    char = char or '*'
    result = []
    line = ''
    for i in range(1, n_floors + 1):
        if i < 3:
            line += char * i
        else:
            line = char * (len(line) + 2)
        result.append(line)

    length = len(result[-1])
    return [x.center(length) for x in result]


def tower1(n_floors: int, char: str | None = None) -> list:
    """Construção de piramide ascii."""
    char = char or '*'
    result = []
    for i in range(1, n_floors + 1):
        line = char * (i * 2 - 1)
        result.append(line.center(n_floors * 2 - 1))
    return result


def tower(n_floors: int, char: str | None = None) -> list:
    """Construção de piramide ascii."""
    char = char or '*'
    return [
        (char * (i * 2 - 1)).center(n_floors * 2 - 1)
        for i in range(1, n_floors + 1)
    ]


if __name__ == '__main__':
    pprint(tower(26))
