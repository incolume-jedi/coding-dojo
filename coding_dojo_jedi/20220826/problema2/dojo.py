def tabuada(tabuada: int, inicial: int = 1, final: int = 10):
    result = []
    inicial, final = min(inicial, final), max(inicial, final)
    for x in range(inicial, final + 1):
        s = f'{tabuada} X {x} = {tabuada * x}'
        result.append(s)
    return result


if __name__ == '__main__':
    print(tabuada(10))
