# def conceito(*args, **kwargs):
#     media = sum(args)/len(args) \
#         if args else (kwargs.get('nota1') + kwargs.get('nota2'))/2
#     return media

def conceito(nota1, nota2):
    return (nota1+nota2)/2
