"""Test for dojo."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20220805.dojo20220805 import bmi


@pytest.mark.parametrize(
    ('peso', 'altura', 'esperado'),
    [
        (50, 1.80, 'Underweight'),
        (80, 1.80, 'Normal'),
        (90, 1.80, 'Overweight'),
        (110, 1.80, 'Obese'),
        (50, 1.50, 'Normal'),
        (70, 1.50, 'Obese'),
    ],
)
def test_bmi0(peso, altura, esperado) -> None:
    """Test bmi."""
    assert bmi(peso, altura) == esperado


@pytest.mark.parametrize(
    ('peso', 'altura', 'esperado'),
    [
        (50, 1.80, 'Underweight'),
        (80, 1.80, 'Normal'),
        (90, 1.80, 'Overweight'),
        (110, 1.80, 'Obese'),
        (50, 1.50, 'Normal'),
        (70, 1.50, 'Obese'),
    ],
)
def test_bmi(peso, altura, esperado) -> None:
    """Test bmi."""
    assert bmi(peso, altura) == esperado
