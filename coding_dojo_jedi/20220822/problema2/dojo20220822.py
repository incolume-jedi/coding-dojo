def calc(quantia: int, preco: float = 2_18) -> float:
    return quantia * preco / 100

def table():
    result = {x: calc(x) for x in range(1, 51)}
    result.update({x: calc(x) for x in range(60, 101, 10)})
    return result


def show():
    for i, j in table().items():
        print(f'{i:4} = R$ {j:6.2f}')
