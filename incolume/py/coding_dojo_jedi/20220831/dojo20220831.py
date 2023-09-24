"""Dojo 2022-08-31."""

# def conceito(*args, **kwargs):
#         if args else (kwargs.get('nota1') + kwargs.get('nota2'))/2


def conceito0(nota1, nota2):
    """Calcula a menção."""
    media = (nota1 + nota2) / 2

    if media >= 9.0:
        return f'Média {media}, "A", APROVADO'
    if 7.5 <= media < 9.0:
        return f'Média {media}, "B", APROVADO'
    if 6.0 <= media < 7.5:
        return f'Média {media}, "C", APROVADO'
    if 4.0 <= media < 6.0:
        return f'Média {media}, "D", REPROVADO'
    return f'Média {media}, "E", REPROVADO'


def conceito1(nota1, nota2):
    """FAIL..."""
    media = (nota1 + nota2) / 2
    if media < 4:
        return f'Média {media}, "E", REPROVADO'
    if 4.0 >= media < 6.0:
        return f'Média {media}, "D", REPROVADO'
    if 6.0 >= media < 7.5:
        return f'Média {media}, "C", APROVADO'
    if 7.5 >= media < 9.0:
        return f'Média {media}, "B", APROVADO'
    return f'Média {media}, "A", APROVADO'


def conceito(nota1, nota2):
    """Calcula a menção."""
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
