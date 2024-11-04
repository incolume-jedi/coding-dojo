"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

from statistics import median

__author__ = '@britodfbr'  # pragma: no cover


def analise_nota():
    """Analise de notas."""
    notas = []
    result = ''
    try:
        while (nota := int(input('Informe a nota: '))) != '-1':
            if nota > -1:
                notas.append(nota)
    except StopIteration:
        pass
    result += f'quantidade: {len(notas)};\n'
    result += f'Notas: {" ".join(str(n) for n in notas)};\n'
    result += f'Reverso: {" ".join(str(n) for n in notas[::-1])};\n'
    result += f'Soma: {sum(notas)};'
    result += f'Média: {(media := median(notas))};'
    result += (
        f'Acima da média: {" ".join(str(n) for n in notas if n >= media)};'
    )
    result += (
        f'Abaixo de {(num := 7)}: '
        f'{" ".join(str(n) for n in notas if n < num)};'
    )
    result += 'Bye bye.'
    print(result)  # noqa: T201


if __name__ == '__main__':  # pragma: no cover
    analise_nota()
