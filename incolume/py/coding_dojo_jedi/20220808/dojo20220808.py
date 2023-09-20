"""Dojo."""


def is_par0(num: int) -> str:
    """Verifica se é Par."""
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'


def is_par(num: int) -> str:
    """Verifica se é Par."""
    if not num:
        msg = 'Valor inválido.'
        raise ValueError(msg)
    if not isinstance(num, int):
        msg = 'Somente números inteiros.'
        raise TypeError(msg)

    return ['Par', 'Ímpar'][num % 2]


if __name__ == '__main__':
    is_par(3 + 0j)
