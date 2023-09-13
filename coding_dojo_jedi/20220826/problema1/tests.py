import pytest
from dojo import no_exclamation



@pytest.mark.parametrize(
    ['entrance', 'expected'],
    (
        ("Hello World!", "Hello World"),
        ("Hello World!!!", "Hello World"),
        ("Hi! Hello!", "Hi Hello"),
        ("", ""),
        ("Oh, no!!!", "Oh, no"),
    )
)
def test_noexclamation(entrance, expected):
    assert no_exclamation(entrance) == expected
