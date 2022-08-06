import pytest
from dojo import bmi


@pytest.mark.parametrize(
    ['peso', 'altura', 'esperado'],
    [
        (50, 1.80, "Underweight"),
        (80, 1.80, "Normal"),
        (90, 1.80, "Overweight"),
        (110, 1.80, "Obese"),
        (50, 1.50, "Normal"),
    ]
)
def test_bmi(peso, altura, esperado):
    assert bmi(peso, altura) ==  esperado
