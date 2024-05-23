"""Test for dojo."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20220810.dojo20220810 import (
    is_vogal0,
    is_vogal1,
    is_vogal2,
    is_vogal,
)


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        ('a', True),
        ('c', False),
        ('b', False),
        ('k', False),
        ('w', False),
        ('y', False),
        ('x', False),
        ('e', True),
        ('i', True),
        ('o', True),
        ('u', True),
        ('p', False),
        ('r', False),
    ],
)
def test_is_vogal0(entrance, expected) -> None:
    """Test is_vogal."""
    assert is_vogal0(entrance) == expected


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        ('a', True),
        ('c', False),
        ('b', False),
        ('k', False),
        ('w', False),
        ('y', False),
        ('x', False),
        ('e', True),
        ('i', True),
        ('o', True),
        ('u', True),
        ('p', False),
        ('r', False),
    ],
)
def test_is_vogal1(entrance, expected) -> None:
    """Test is_vogal."""
    assert is_vogal1(entrance) == expected


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        ('a', True),
        ('c', False),
        ('b', False),
        ('k', False),
        ('w', False),
        ('y', False),
        ('x', False),
        ('e', True),
        ('i', True),
        ('o', True),
        ('u', True),
        ('p', False),
        ('r', False),
    ],
)
def test_is_vogal2(entrance, expected) -> None:
    """Test is_vogal."""
    assert is_vogal2(entrance) == expected


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        ('a', True),
        ('c', False),
        ('b', False),
        ('k', False),
        ('w', False),
        ('y', False),
        ('x', False),
        ('e', True),
        ('i', True),
        ('o', True),
        ('u', True),
        ('p', False),
        ('r', False),
    ],
)
def test_is_vogal(entrance, expected) -> None:
    """Test is_vogal."""
    assert is_vogal(entrance) == expected
