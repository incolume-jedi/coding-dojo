"""Dojo."""

DIAS = [
    'domingo',
    'segunda-feira',
    'terça-feira',
    'quarta-feira',
    'quinta-feira',
    'sexta-feira',
    'sábado',
]

SEMANA = dict(enumerate(DIAS))


def weekday0(dia: str, qtd: int) -> str:
    """Exibe dias da semana."""
    for i in range(len(DIAS)):
        if dia == DIAS[i]:
            return DIAS[(DIAS.index(dia) + qtd) % 7]
    return ''


def weekday(dia: str, qtd: int) -> str:
    """Exibe dias da semana."""
    for i, dia_semana in enumerate(DIAS):
        print(i, dia_semana)
        if dia == dia_semana:
            return DIAS[(DIAS.index(dia) + qtd) % 7]
    return ''


if __name__ == '__main__':
    print(weekday('domingo', 1))