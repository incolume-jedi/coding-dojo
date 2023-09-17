def weekday(dia: str, qtd: int) -> str:
    dias = [
        'domingo',
        'segunda-feira',
        'terça-feira',
        'quarta-feira',
        'quinta-feira',
        'sexta-feira',
        'sábado',
    ]

    for i in range(len(dias)):
        # print(i, dias[i])
        if dia == dias[i]:
            return dias[(dias.index(dia) + qtd % 7) % 7]
        # return dias.index(dia)


if __name__ == '__main__':
    print(weekday('domingo', 1))
