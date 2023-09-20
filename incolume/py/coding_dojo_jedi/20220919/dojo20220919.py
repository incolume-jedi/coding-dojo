"""Dojo."""


def weekday(number_day: int) -> str:
    """Retorna o dia da semana a partir do número."""
    dias_semana = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado',
    }
    if number_day not in dias_semana:
        msg = 'Valor Inválido'
        raise ValueError(msg)
    return dias_semana.get(number_day)
