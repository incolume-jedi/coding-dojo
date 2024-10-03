"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241001 as pkg
import pytest


class TestCase:
    """Test case class."""

    t0: ClassVar = [
        (
            {'á': [0], 'a': [3], 'g': [1], 'u': [2]},
            'água',
        ),
        (
            {'a': [0, 2], 'c': [1], 'í': [3]},
            'açaí',
        ),
        (
            {'a': [0], 'z': [1], 'u': [2], 'l': [3]},
            'azul',
        ),
        (
            {
                'a': [0, 3, 5, 7, 10],
                'b': [1, 8],
                'r': [2, 9],
                'c': [4],
                'd': [6],
            },
            'abracadabra',
        ),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        t0,
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected
