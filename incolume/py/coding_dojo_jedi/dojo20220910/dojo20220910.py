"""Dojo."""


def weekday0(num: int) -> str:
    """Retorna o dia da semana.

    implementação if elif
    """
    if num == 1:
        resposta = 'Domingo'
    elif num == 2:
        resposta = 'Segunda'
    elif num == 3:
        resposta = 'Terça'
    elif num == 4:
        resposta = 'Quarta'
    elif num == 5:
        resposta = 'Quinta'
    elif num == 6:
        resposta = 'Sexta'
    elif num == 7:
        resposta = 'Sábado'
    else:
        resposta = 'Valor inválido'
    return resposta


def weekday1(num: int) -> str:
    """Retorna o dia da semana.

    implementação dict
    """
    semana = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado',
    }
    return semana.get(num, 'Valor inválido')


try:

    def weekday(num: int) -> str:
        """Retorna o dia da semana.

        implementação match case.
        """
        match num:
            case 1:
                return 'Domingo'
            case 2:
                return 'Segunda'
            case 3:
                return 'Terça'
            case 4:
                return 'Quarta'
            case 5:
                return 'Quinta'
            case 6:
                return 'Sexta'
            case 7:
                return 'Sábado'
            case _:
                return 'Valor inválido'

except SyntaxError as err:
    MSG = 'This run only Python 3.10+'
    raise OSError(MSG) from err


if __name__ == '__main__':    # pragma: no cover
    from dis import dis

    dis(weekday0)
    dis(weekday1)
    dis(weekday)
