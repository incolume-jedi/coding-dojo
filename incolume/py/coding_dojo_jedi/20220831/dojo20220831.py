# def conceito(*args, **kwargs):
#         if args else (kwargs.get('nota1') + kwargs.get('nota2'))/2


def conceito0(nota1, nota2):
    media = (nota1 + nota2) / 2

    if media >= 9.0 and media <= 10:
        return f'Média {media}, "A", APROVADO'
    elif media >= 7.5 and media < 9.0:
        return f'Média {media}, "B", APROVADO'
    elif media >= 6.0 and media < 7.5:
        return f'Média {media}, "C", APROVADO'
    elif media >= 4.0 and media < 6.0:
        return f'Média {media}, "D", REPROVADO'
    else:
        return f'Média {media}, "E", REPROVADO'


def conceito1(nota1, nota2):
    """FAIL..."""
    media = (nota1 + nota2) / 2
    if media < 4:
        return f'Média {media}, "E", REPROVADO'
    elif 4.0 >= media < 6.0:
        return f'Média {media}, "D", REPROVADO'
    elif 6.0 >= media < 7.5:
        return f'Média {media}, "C", APROVADO'
    elif 7.5 >= media < 9.0:
        return f'Média {media}, "B", APROVADO'
    else:
        return f'Média {media}, "A", APROVADO'


def conceito(nota1, nota2):
    media = (nota1 + nota2) / 2
    mencao = {
        'A': 'APROVADO',
        'B': 'APROVADO',
        'C': 'APROVADO',
        'D': 'REPROVADO',
        'E': 'REPROVADO',
    }
    result = list(mencao.keys())[::-1][
        (media >= 9) + (media >= 7.5) + (media >= 6) + (media >= 4)
    ]
    return f'Média {media}, "{result}", {mencao.get(result)}'
