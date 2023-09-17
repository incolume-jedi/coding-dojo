import pytest
import dojo20220717


def test_dojo202207171():
    assert dojo20220717.palindrome('Python') == False


def test_dojo202207172():
    assert dojo20220717.palindrome('anna') == True


@pytest.mark.parametrize(
    ['entrada', 'esperado'],
    (
        ('walter', False),
        (12321, True),
        (123456, False),
        ('ada', True),
    ),
)
def test_dojo20220717(entrada, esperado):
    assert dojo20220717.palindrome(entrada) == esperado
