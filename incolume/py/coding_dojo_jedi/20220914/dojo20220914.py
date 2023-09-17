DIAS = [
    'domingo',
    'segunda-feira',
    'terça-feira',
    'quarta-feira',
    'quinta-feira',
    'sexta-feira',
    'sábado',
]

SEMANA = {x: y for x, y in enumerate(DIAS)}


def weekday0(dia: str, qtd: int) -> str:
    for i in range(len(DIAS)):
        if dia == DIAS[i]:
            return DIAS[(DIAS.index(dia) + qtd) % 7]


def weekday(dia: str, qtd: int) -> str:
    for i, dia_semana in enumerate(DIAS):
        print(i, dia_semana)
        if dia == dia_semana:
            return DIAS[(DIAS.index(dia) + qtd) % 7]


if __name__ == '__main__':
    print(weekday('domingo', 1))
