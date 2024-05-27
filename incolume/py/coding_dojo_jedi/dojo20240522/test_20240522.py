"""Test module."""

import pytest
from . import is_palindrome


class TestCase:
    """Test case."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                -232,
                {
                    'expected_exception': ValueError,
                    'match': 'limited : -231 <= x <= 232',
                },
            ),
            (
                233,
                {
                    'expected_exception': ValueError,
                    'match': 'limited : -231 <= x <= 232',
                },
            ),
        ],
    )
    def test_restrictions(self, entrance, expected):
        """Restrictions."""
        with pytest.raises(**expected):
            is_palindrome(entrance)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (121, True),
            (-121, False),
            (10, False),
        ],
    )
    def test_funcionalidade(self, entrance, expected):
        """Test funcionalidade."""
        assert is_palindrome(entrance) == expected
