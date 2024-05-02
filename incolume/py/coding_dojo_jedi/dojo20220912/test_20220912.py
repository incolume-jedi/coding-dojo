"""Testing dojo."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20220912.dojo20220912 import (
    weekday,
    weekday0,
)


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        (('sábado', 1), 'domingo'),
        (('quinta-feira', 3), 'domingo'),
        (('segunda-feira', 1), 'terça-feira'),
        (('terça-feira', 0), 'terça-feira'),
        (('terça-feira', 1), 'quarta-feira'),
        (('terça-feira', 2), 'quinta-feira'),
        (('terça-feira', 3), 'sexta-feira'),
        (('terça-feira', 4), 'sábado'),
        (('terça-feira', 5), 'domingo'),
        (('terça-feira', 6), 'segunda-feira'),
        (('terça-feira', 7), 'terça-feira'),
        (('terça-feira', 180), 'domingo'),
    ],
)
def test_weekday0(entrance, expected) -> None:
    """Unittest for weekday0."""
    assert weekday0(*entrance) == expected


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        (('sábado', 1), 'domingo'),
        (('quinta-feira', 3), 'domingo'),
        (('segunda-feira', 1), 'terça-feira'),
        (('terça-feira', 0), 'terça-feira'),
        (('terça-feira', 1), 'quarta-feira'),
        (('terça-feira', 2), 'quinta-feira'),
        (('terça-feira', 3), 'sexta-feira'),
        (('terça-feira', 4), 'sábado'),
        (('terça-feira', 5), 'domingo'),
        (('terça-feira', 6), 'segunda-feira'),
        (('terça-feira', 7), 'terça-feira'),
        (('terça-feira', 180), 'domingo'),
    ],
)
def test_weekday(entrance, expected) -> None:
    """Unittest for weekday."""
    assert weekday(*entrance) == expected
