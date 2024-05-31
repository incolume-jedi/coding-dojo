"""Module."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20240531 import (
    last_dig,
    last_dig0,
    last_dig1,
)

__author__ = '@britodfbr'  # pragma: no cover


@pytest.mark.parametrize(
    'function entrance expected'.split(),
    [
        (last_dig0, (2, 27), 8),
        (last_dig1, (2, 27), 8),
        (last_dig, (2, 27), 8),
    ],
)
def test_last_dig(function, entrance, expected):
    """Test last_dig."""
    assert function(*entrance) == expected
