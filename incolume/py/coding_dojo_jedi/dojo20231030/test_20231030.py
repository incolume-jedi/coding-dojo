"""Clean Code in Python - Chapter 01.

Introcution, Tools, and Formatting
Tests for annotations examples
"""

import pytest

from incolume.py.coding_dojo_jedi.dojo20231030.dojo20231030 import (
    NewPoint,
    Point,
    int_reverso,
    locate,
)


@pytest.mark.parametrize(
    'element expected'.split(),
    [
        pytest.param(
            Point,
            {},
        ),
        (locate, {'latitude': float, 'longitude': float, 'return': Point}),
        (NewPoint, {'lat': float, 'long': float}),
    ],
)
def test_annotations(element, expected) -> None:
    """Test the class/functions againts its expected annotations."""
    method = '__annotations__'
    assert getattr(element, method) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [(123, 321), (-123, -321), (120, 21), (102, 201), (123456789, 987654321)],
)
def test_int_reverso(entrance, expected) -> None:
    """Teste int_reverso."""
    assert int_reverso(entrance) == expected
