"""Clean Code in Python - Chapter 01: Introcution, Tools, and Formatting

Tests for annotations examples

"""
import pytest

from incolume.py.coding_dojo_jedi.dojo20231030.dojo  import NewPoint, Point, locate


@pytest.mark.parametrize(
    "element,expected",
    (
        pytest.param(
            Point, 
            {}, 
            # marks=pytest.mark.skip(reason='fail.')
        ),
        (locate, {"latitude": float, "longitude": float, "return": Point}),
        (NewPoint, {"lat": float, "long": float}),
    ),
)
def test_annotations(element, expected):
    """test the class/functions againts its expected annotations"""
    assert getattr(element, "__annotations__") == expected