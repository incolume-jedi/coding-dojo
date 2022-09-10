import pytest
from dojo import weekday


@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        (1, 'Domingo'),
        (2, 'Segunda'),
        (3, 'Terça'),
        (4, 'Quarta'),
        (5, 'Quinta'),
        (6, 'Sexta'),
        (7, 'Sábado'),
        (8, 'Valor inválido'),
        (9, 'Valor inválido'),
    ),
)
def test_weekday(entrance, expected):
    assert weekday(entrance) == expected
