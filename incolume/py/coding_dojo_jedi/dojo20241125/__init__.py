"""dojo module."""

from string import ascii_letters


def validate_rules(frase: str, maximum: int = 100) -> bool:
    """Validade rules."""
    msg = ''
    valided = range(33, 123)
    excluded = [34, 39]

    if len(frase) > maximum:
        msg = 'Tamanho da frase deve ser entre 1 e 100 caracteres.'
        raise SyntaxError(msg)

    for char in frase:
        c = ord(char)
        if c not in valided:
            msg = 'Letras inválidas para frase.'
            raise ValueError(msg)
        if c in excluded:
            msg = 'Caracteres inválidos: \' ou "'
            raise SyntaxError(msg)


def dojo(frase: str) -> str:
    """Dojo solution."""
    pos = 0
    validate_rules(frase)
    simbols = {}
    result = []

    for pos, item in enumerate(frase):
        if item in ascii_letters:
            result.insert(0, item)
        else:
            simbols[pos] = item

    for idx, item in simbols.items():
        result.insert(idx, item)

    return ''.join(result)
