def no_exclamation0(frase: str) -> str:
    result = ''
    for letra in frase:
        if letra != '!':
            result += letra
    return result


def no_exclamation1(frase: str) -> str:
    return ''.join(x for x in frase if x != '!')


def no_exclamation(frase: str) -> str:
    return frase.replace('!', '')

