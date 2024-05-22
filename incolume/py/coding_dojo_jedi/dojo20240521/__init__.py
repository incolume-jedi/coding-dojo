"""Dojo module."""

import datetime
import locale
from statistics import median

import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta
from pytz import timezone

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

tz: timezone = timezone('America/Sao_Paulo')


def temp0(**kwargs: list[int]) -> str:
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


def temp1(**kwargs: list[int]) -> str:
    """Media de temperatura."""
    meses = {
        mes.strftime('%B'): []
        for mes in pd.date_range(
            start='2021-01-01',
            end='2021-12-31',
            periods=12,
        )
    }

    meses['média anual'] = median(median(mes) for mes in kwargs.values())
    for mes, temps in kwargs.items():
        meses[mes] = list({t for t in temps if t > meses['média anual']})
    return meses


def temp(**kwargs: list[int]) -> str:
    """Media de temperatura."""
    meses = {
        mes.strftime('%B'): []
        for mes in np.arange(
            '2009-01',
            '2010-01',
            dtype='datetime64[M]',
        ).astype(datetime.datetime)
    }

    meses['média anual'] = median(median(mes) for mes in kwargs.values())
    for mes, temps in kwargs.items():
        meses[mes] = list({t for t in temps if t > meses['média anual']})
    return meses
