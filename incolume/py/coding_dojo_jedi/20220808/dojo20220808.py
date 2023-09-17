from types import NoneType


def is_par0(num: int) -> str:
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'


def is_par(num: int) -> str:
    if isinstance(num, NoneType):
        msg = 'Valor inválido.'
        raise ValueError(msg)
    if not isinstance(num, int):
        msg = 'Somente números inteiros.'
        raise TypeError(msg)

    return ['Par', 'Ímpar'][num % 2]


if __name__ == '__main__':
    is_par(3 + 0j)
