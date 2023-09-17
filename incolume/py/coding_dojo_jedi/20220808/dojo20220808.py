from types import NoneType


def is_par0(num: int) -> str:
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'


def is_par(num: int) -> str:
    if isinstance(num, NoneType):
        raise ValueError('Valor inválido.')
    if not isinstance(num, int):
        raise TypeError('Somente números inteiros.')

    return ['Par', 'Ímpar'][num % 2]


if __name__ == '__main__':
    is_par((3 + 0j))
