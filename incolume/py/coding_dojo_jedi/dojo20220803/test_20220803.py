"""Test for dojo."""
import pytest

from incolume.py.coding_dojo_jedi.dojo20220803.dojo20220803 import cavaleiro


@pytest.mark.parametrize(
    ('balas', 'dragoes', 'sobreviver'),
    [
        (3, 5, False),
        (10, 5, True),
        (9, 5, False),
    ],
)
def test_cavaleiro(balas, dragoes, sobreviver) -> None:
    """Test cavaleiro."""
    assert cavaleiro(balas, dragoes) == sobreviver
