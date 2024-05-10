"""Module."""

import pytest


from . import is_narcisist


__author__ = '@britodfbr'  # pragma: no cover


class TestNarcisista:
    """Caso test number narcisist."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (1, True),
            (10, False),
            (153, True),
            (222, False),
            (1634, True),
            (1111, False),
        ],
    )
    def test_is_narcisist(self, entrance, expected):
        """Test if is narcisist number."""
        assert is_narcisist(entrance) == expected
