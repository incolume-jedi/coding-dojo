def no_exclamation0(frase: str) -> str:
    """Problema 1."""
    result = ""
    for letra in frase:
        if letra != "!":
            result += letra
    return result


def no_exclamation1(frase: str) -> str:
    """Problema 1."""
    return "".join(x for x in frase if x != "!")


def no_exclamation(frase: str) -> str:
    """Problema 1."""
    return frase.replace("!", "")


def tabuada(tabuada: int, inicial: int = 1, final: int = 10):
    """Problema 2."""
    result = []
    inicial, final = min(inicial, final), max(inicial, final)
    for x in range(inicial, final + 1):
        s = f"{tabuada} X {x} = {tabuada * x}"
        result.append(s)
    return result


def imc(altura: float, peso: float) -> str:
    """Problema 3."""
    imc = peso / altura**2
    return [
        "Obesidade III",
        "Obesidade II",
        "Obesidade I",
        "Sobrepeso",
        "peso normal",
        "abaixo do peso",
    ][(imc < 39.9) + (imc < 34.9) + (imc < 29.9) + (imc < 24.9) + (imc < 18.5)]
