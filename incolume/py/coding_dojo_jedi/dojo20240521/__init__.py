"""Dojo module."""

import datetime
import locale
from statistics import median

from dateutil.relativedelta import relativedelta
from pytz import timezone

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

tz: timezone = timezone('America/Sao_Paulo')


def temp(**kwargs: list[int]) -> str:
    """Media de temperatura."""
    meses = {
        (
            datetime.datetime(2000, 1, 1, tzinfo=tz) + relativedelta(month=+x)
        ).strftime(
            '%B',
        ): []
        for x in range(13)
    }
    meses['média anual'] = median(median(mes) for mes in kwargs.values())
    for mes, temps in kwargs.items():
        meses[mes] = list({t for t in temps if t > meses['média anual']})
    return meses
