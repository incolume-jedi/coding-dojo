"""Dojo module."""

import datetime
from statistics import median
from typing import Final

import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta
from pytz import timezone

tz: timezone = timezone('America/Sao_Paulo')

MESES: Final[dict[str, str]] = {
    '01': 'janeiro',
    '02': 'fevereiro',
    '03': 'março',
    '04': 'abril',
    '05': 'maio',
    '06': 'junho',
    '07': 'julho',
    '08': 'agosto',
    '09': 'setembro',
    '10': 'outubro',
    '11': 'novembro',
    '12': 'dezembro',
}


def temp0(**kwargs: list[int]) -> str:
    """Media de temperatura."""
    meses = {
        MESES.get(
            (
                datetime.datetime(2000, 1, 1, tzinfo=tz)
                + relativedelta(month=+x)
            ).strftime(
                '%m',
            ),
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
        MESES.get(mes.strftime('%m')): []
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
        MESES.get(mes.strftime('%m')): []
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
