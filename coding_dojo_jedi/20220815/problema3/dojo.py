def adedonha(num: int) -> str:
    alfabeto = 'abcdefghijklmnopqrstuvxwyz'
    return alfabeto[num % len(alfabeto) - 1]
