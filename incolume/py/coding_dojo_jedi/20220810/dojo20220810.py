def is_vogal0(letra: str) -> bool:
    vogais = ['a', 'e', 'i', 'o', 'u']
    return any(letra == vogal for vogal in vogais)


def is_vogal1(letra: str) -> bool:
    vogais = ['a', 'e', 'i', 'o', 'u']
    if letra in vogais:
        return True
    return False


def is_vogal(letra: str) -> bool:
    vogais = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
    return vogais.get(letra, False)
