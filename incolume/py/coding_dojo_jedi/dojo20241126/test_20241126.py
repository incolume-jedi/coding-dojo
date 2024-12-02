"""Test module."""

import sys
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241126 as pkg
import pytest
from dataclasses import asdict
import copy


pytest.mark.skipif(
    sys.version_info < (3, 13),
    reason='requires python3.13 or higher',
)


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                {'name': 'cup', 'cost': 10.0},
                {'name': 'goldcup', 'cost': 100.0},
            ),
            (
                {'name': 'cup', 'cost': 10.0},
                {'name': 'goldcup'},
            ),
            (
                {'name': 'cup', 'cost': 10.0},
                {'cost': 100.0},
            ),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        element = pkg.dojo(**entrance)
        item: pkg.Item = copy.replace(element, **expected)
        assert asdict(item) == {**asdict(item), **expected}
