import pytest
from dojo import cavaleiro


@pytest.mark.parametrize(
    ["balas", "dragoes", "sobreviver"],
    [
        (3, 5, False),
        (10, 5, True),
        (9, 5, False),
    ]
)
def test_cavaleiro(balas, dragoes, sobreviver):
    assert cavaleiro(balas, dragoes) == sobreviver
