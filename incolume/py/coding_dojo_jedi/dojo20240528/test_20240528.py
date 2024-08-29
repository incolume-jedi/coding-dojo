"""Module."""

from . import all_permutations

import pytest


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (
            (1, 2, 3),
            [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)],
        ),
        (
            '123',
            [
                ('1', '2', '3'),
                ('1', '3', '2'),
                ('2', '1', '3'),
                ('2', '3', '1'),
                ('3', '1', '2'),
                ('3', '2', '1'),
            ],
        ),
        (
            'ACGT',
            [
                ('A', 'C', 'G', 'T'),
                ('A', 'C', 'T', 'G'),
                ('A', 'G', 'C', 'T'),
                ('A', 'G', 'T', 'C'),
                ('A', 'T', 'C', 'G'),
                ('A', 'T', 'G', 'C'),
                ('C', 'A', 'G', 'T'),
                ('C', 'A', 'T', 'G'),
                ('C', 'G', 'A', 'T'),
                ('C', 'G', 'T', 'A'),
                ('C', 'T', 'A', 'G'),
                ('C', 'T', 'G', 'A'),
                ('G', 'A', 'C', 'T'),
                ('G', 'A', 'T', 'C'),
                ('G', 'C', 'A', 'T'),
                ('G', 'C', 'T', 'A'),
                ('G', 'T', 'A', 'C'),
                ('G', 'T', 'C', 'A'),
                ('T', 'A', 'C', 'G'),
                ('T', 'A', 'G', 'C'),
                ('T', 'C', 'A', 'G'),
                ('T', 'C', 'G', 'A'),
                ('T', 'G', 'A', 'C'),
                ('T', 'G', 'C', 'A'),
            ],
        ),
    ],
)
def test_permitation(entrance, expected):
    """Test it."""
    assert all_permutations(entrance) == expected
