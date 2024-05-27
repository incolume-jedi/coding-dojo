"""Module."""

__author__ = '@britodfbr'  # pragma: no cover

from typing import ClassVar

import pytest
from . import soma, soma0, soma_pythonic


class Testcase:
    """Test case."""

    case_0: ClassVar = [
        (896, 23),
        (111, 3),
        (1000000000000000, 1),
        (900000000001, 10),
        (321, 6),
        (123, 6),
        (21, 3),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        case_0,
    )
    def test_soma0(self, entrance, expected):
        """Test it."""
        assert soma0(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        case_0,
    )
    def test_soma(self, entrance, expected):
        """Test it."""
        assert soma(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        case_0,
    )
    def test_soma_py(self, entrance, expected):
        """Test it."""
        assert soma_pythonic(entrance) == expected
