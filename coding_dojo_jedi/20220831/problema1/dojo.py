# def conceito(*args, **kwargs):
#     media = sum(args)/len(args) \
#         if args else (kwargs.get('nota1') + kwargs.get('nota2'))/2
#     return media

def conceito(nota1, nota2):
    media = (nota1+nota2)/2

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



