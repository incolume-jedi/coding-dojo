"""Test module."""

import pytest
from . import feliz


class TestFeliz:
    """Test case."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (1, True),
            (2, False),
            (3, False),
            (4, False),
            (7, True),
            (19, True),
        ],
    )
    def test_feliz(self, entrance, expected):
        """Test it."""
        assert feliz(entrance) == expected
