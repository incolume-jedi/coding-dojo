"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241001 as pkg
import pytest


class TestCase:
    """Test case class."""

    t0: ClassVar = [
        pytest.param(
            {'a': [1, 3], 'p': [0, 2]},
            'papa',
            marks=[],
        ),
        pytest.param(
            {'á': [0], 'a': [3], 'g': [1], 'u': [2]},
            'água',
            marks=[],
        ),
        pytest.param(
            {'a': [0, 2], 'ç': [1], 'í': [3]},
            'açaí',
            marks=[],
        ),
        pytest.param(
            {'a': [0], 'z': [1], 'u': [2], 'l': [3]},
            'azul',
            marks=[],
        ),
        pytest.param(
            {
                'i': [1, 4, 7, 9],
                'm': [0],
                's': [2, 3, 5, 6],
                'p': [8],
            },
            'mississipi',
            marks=[],
        ),
        pytest.param(
            {
                'p': [8],
                'i': [1, 4, 7, 9],
                'm': [0],
                's': [2, 3, 5, 6],
            },
            'mississipi',
            marks=[],
        ),
        pytest.param(
            {
                'd': [6],
                'c': [4],
                'a': [0, 3, 5, 7, 10],
                'r': [2, 9],
                'b': [1, 8],
            },
            'abracadabra',
            marks=[],
        ),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        t0,
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected
