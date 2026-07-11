"""Test module."""

from __future__ import annotations
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20260711 as pkg
import pytest


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        ['entrance1', 'entrance2', 'expected'],
        [
            pytest.param(
                (1, 2, 3),
                {'a': 1, 'b': 2, 'c': 3},
                {
                    'a': 1,
                    'b': 2,
                    'c': 3,
                    'args': (
                        1,
                        2,
                        3,
                    ),
                },
                marks=[],
            ),
        ],
    )
    def test_0(self, entrance1, entrance2, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(*entrance1, **entrance2) == expected
