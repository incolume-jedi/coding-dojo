"""dojo module."""


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
    frase = frase.casefold()
    alphabet = range(97, 123)
    other = {}
    result, temp = '', ''

    validate_rules(frase)

    for idx, char in enumerate(frase):
        c = ord(char)
        if c in alphabet:
            temp += char
        else:
            other[idx] = char

    for idx, char in enumerate(temp[::-1]):
        if idx in other:
            result += other[idx]
        result += char

    return result
