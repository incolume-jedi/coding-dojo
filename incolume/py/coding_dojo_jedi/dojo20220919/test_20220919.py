import pytest
from dojo20220919 import weekday


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    (
        (1, 'Domingo'),
        (2, 'Segunda'),
        (3, 'Terça'),
        (4, 'Quarta'),
        (5, 'Quinta'),
        (6, 'Sexta'),
        (7, 'Sábado'),
        (0, {'expected_exception': ValueError, 'match': 'Valor Inválido'}),
        (8, {'expected_exception': ValueError, 'match': 'Valor Inválido'}),
        (9, {'expected_exception': ValueError, 'match': 'Valor Inválido'}),
    ),
)
def test_weekday(entrance, expected):
    try:
        with pytest.raises(**expected):
            weekday(entrance)
    except TypeError:
        assert weekday(entrance) == expected
