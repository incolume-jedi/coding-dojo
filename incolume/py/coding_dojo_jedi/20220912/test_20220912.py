import pytest
from dojo20220912 import weekday


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    (
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
    ),
)
def test_weekday(entrance, expected):
    assert weekday(*entrance) == expected
