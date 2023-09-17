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
        if dia == dias[i]:
            return dias[(dias.index(dia) + qtd % 7) % 7]
    return None


if __name__ == '__main__':
    print(weekday('domingo', 1))
