"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20240917 as pkg
import pytest


class TestLongestPalindromeSubString:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected exception'.split(),
        [
            ('cbbd', 'bb', None),
            ('forgeeksskeegfor', 'geeksskeeg', None),
            ('nave', '', None),
            (
                'çaç',
                'çaç',
                {
                    'expected_exception': UnicodeError,
                    'match': 'Not ASCII characters.',
                },
            ),
            (
                'a' * 1001,
                '',
                {
                    'expected_exception': ValueError,
                    'match': 'Limit until 1000 characters.',
                },
            ),
            (
                'çüç',
                '',
                {
                    'expected_exception': UnicodeError,
                    'match': 'Not ASCII characters.',
                },
            ),
        ],
    )
    def test_0(self, exception, entrance, expected) -> NoReturn:
        """Unittest."""
        if exception:
            with pytest.raises(**exception):
                pkg.dojo(entrance)
        else:
            assert pkg.dojo(entrance) == expected
