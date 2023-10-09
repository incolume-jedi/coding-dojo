import pytest
from . import max_sequence, maxSubArraySum



def test_max_sequence():
    """Test de max_sequence."""
    assert max_sequence([]) == 0


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ([-1, -2, -3, -4], 0),
        ([-10, -2, -3, -1], 0),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 45),
        ([10, 1, 2, 3, 4, 5, 6, 7, 8, 9], 55),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([10, -11, 2, 3, 4, 5, -5,  6, 7, -50, 8,-7, 9],14),
        ([-2, -3, 4, -1, -2, 1, 5, -3], 7),
    ],
)
def test_max_sequence1(entrance, expected):
    """Test de max."""
    assert max_sequence(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ([-1, -2, -3, -4], 0),
        ([-10, -2, -3, -1], 0),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 45),
        ([10, 1, 2, 3, 4, 5, 6, 7, 8, 9], 55),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([10, -11, 2, 3, 4, 5, -5,  6, 7, -50, 8,-7, 9],14),
        ([-2, -3, 4, -1, -2, 1, 5, -3], 7),
    ],
)
def test_maxSubArraySum(entrance, expected):
    """Test maxSubArraySum."""
    assert  maxSubArraySum(entrance) == expected
