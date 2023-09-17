import pytest
import dojo20220714


@pytest.mark.parametrize(
    ["entrance", "expected"],
    (
        ("Python", "nohtyP"),
        ("Brasil", "lisarB"),
        ("Ada", "adA"),
        ("Ana", "anA"),
    ),
)
def test_rev(entrance, expected):
    assert dojo20220714.rev(entrance) == expected
