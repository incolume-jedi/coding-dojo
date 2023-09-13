import pytest
from dojo import imc


@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        ((1.74, 75), 'peso normal'),
        ((1.54, 125), 'Obesidade III'),
        ((1.72, 80), 'Sobrepeso'),
        ((1.84, 55), 'abaixo do peso'),
        ((1.64, 75), 'Sobrepeso'),
        ((1.84, 135), 'Obesidade II'),
        ((1.78, 95), 'Obesidade I'),
        ((1.78, 98), 'Obesidade I'),
    )
)
def test_imc(entrance, expected):
    assert imc(*entrance) == expected
