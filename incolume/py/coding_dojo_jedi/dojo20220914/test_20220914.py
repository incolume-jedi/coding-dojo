import pytest

from incolume.py.coding_dojo_jedi.dojo20220914.dojo20220914 import weekday


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    (
        (('sábado', 1), 'domingo'),
        (('sábado', 2), 'segunda-feira'),
        (('sábado', 3), 'terça-feira'),
        (('sábado', 4), 'quarta-feira'),
        (('sábado', 5), 'quinta-feira'),
        (('sábado', 6), 'sexta-feira'),
        (('sábado', 7), 'sábado'),
        (('sábado', 0), 'sábado'),
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
    ),
)
def test_weekday(entrance, expected):
    assert weekday(*entrance) == expected
