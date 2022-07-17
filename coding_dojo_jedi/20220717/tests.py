import pytest
import dojo


def test_dojo1():
    assert dojo.palindrome('Python') == False

def test_dojo2():
    assert dojo.palindrome('anna') == True


@pytest.mark.parametrize(
    ['entrada', 'esperado'],
    (
        ("walter", False),
        (12321, True),
        (123456, False),
        ("ada", True),
    )
)
def test_dojo(entrada, esperado):
    assert dojo.palindrome(entrada) == esperado
