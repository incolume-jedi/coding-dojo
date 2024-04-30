"""Testing dojo20220815."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20220815.dojo20220815 import (
    adedonha,
    index,
    index0,
    index1,
)


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        (0, 'P'),
        (6, 'P'),
        (1, 'y'),
        (5, 'n'),
        (2, 't'),
        (1026, 'P'),
        (2048, 't'),
        (3073, 'y'),
        (65536, 'o'),
    ],
)
def test_index0(entrance, expected) -> None:
    """Test intex0."""
    assert index0(entrance) == expected


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        (0, 'P'),
        (6, 'P'),
        (1, 'y'),
        (5, 'n'),
        (2, 't'),
        (1026, 'P'),
        (2048, 't'),
        (3073, 'y'),
        (65536, 'o'),
    ],
)
def test_index1(entrance, expected) -> None:
    """Test index1."""
    assert index1(entrance) == expected


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        (('Python', 0), 'P'),
        (('casa', 6), 's'),
        (('Brasil', 1), 'r'),
        (('Brasília', 4), 'í'),
        (('dojo20220815', 2), 'j'),
        (('xpto', 1026), 't'),
        (('xpto', 2048), 'x'),
        (('xpto', 3073), 'p'),
        (('xpto', 65536), 'x'),
    ],
)
def test_index(entrance, expected) -> None:
    """Test index."""
    assert index(*entrance) == expected


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        (1, 'a'),
        (5, 'e'),
        (26, 'z'),
        (10, 'j'),
        (2, 'b'),
        (3, 'c'),
        (21, 'u'),
        (100, 'v'),
        (80, 'b'),
        (15, 'o'),
        (19, 's'),
        (36, 'j'),
        (1000, 'l'),
    ],
)
def test_adedonha(entrance, expected) -> None:
    """Test adedonha."""
    assert adedonha(entrance) == expected
