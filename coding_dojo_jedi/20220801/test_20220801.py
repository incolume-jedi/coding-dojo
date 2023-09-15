import pytest
from dojo20220801 import square


@pytest.mark.parametrize(
    ("entrada", "esperado"),
    [
        (-1, False),
        (0, True),
        (3, False),
        (4, True),
        (25, True),
        (26, False),
    ],
)
def test_square(entrada, esperado):
    assert square(entrada) == esperado
