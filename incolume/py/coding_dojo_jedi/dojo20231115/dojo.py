"""Dojo 20231115 milissegundos sobrecarga de função."""

import datetime as dt

__author__ = '@britodfbr'  # pragma: no cover


def millisec_int(*, h: int = 0, m: int = 0, s: int = 0) -> int:
    """Calculo de milissegundos para argumentos int."""
    hora = 0, 23
    min_sec = 0, 59
    if not hora[0] <= h <= hora[1]:
        msg = '0 <= h <= 23'
        raise ValueError(msg)

    if not min_sec[0] <= m <= min_sec[1]:
        msg = '0 <= m <= 59'
        raise ValueError(msg)

    if not min_sec[0] <= s <= min_sec[1]:
        msg = '0 <= s <= 59'
        raise ValueError(msg)

    return (h * 3600 + m * 60 + s) * 1000


def millisec_datetime(hms: dt.datetime) -> int:
    """Calculo de milissegundos para argumentos datetime."""
    return millisec_int(h=hms.hour, m=hms.minute, s=hms.second)


def milissegundos(**kwargs) -> int:
    """Calculo de milissegundos."""
    hms = kwargs.get('hms')
    if hms:
        return millisec_datetime(hms)

    h = kwargs.get('h', 0)
    m = kwargs.get('m', 0)
    s = kwargs.get('s', 0)
    return millisec_int(h=h, m=m, s=s)
