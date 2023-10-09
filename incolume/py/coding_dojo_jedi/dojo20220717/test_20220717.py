import pytest

from incolume.py.coding_dojo_jedi.dojo20220717 import dojo20220717


def test_dojo202207171() -> None:
    assert dojo20220717.palindrome('Python') is False


def test_dojo202207172() -> None:
    assert dojo20220717.palindrome('anna') is True


@pytest.mark.parametrize(
    ('entrada', 'esperado'),
    [
        ('walter', False),
        (12321, True),
        (123456, False),
        ('ada', True),
    ],
)
def test_dojo20220717(entrada: str, esperado: bool) -> None:
    assert dojo20220717.palindrome(entrada) == esperado
