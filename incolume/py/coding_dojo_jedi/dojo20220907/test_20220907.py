"""Testing dojo."""
import pytest

from incolume.py.coding_dojo_jedi.dojo20220907.dojo20220907 import fizzbuzz


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (1, '1'),
        (3, 'Fizz'),
        (5, 'Buzz'),
        (7, '7'),
        (15, 'FizzBuzz'),
        (30, 'FizzBuzz'),
        (17, '17'),
        (27, 'Fizz'),
        (10, 'Buzz'),
        (45, 'FizzBuzz'),
        (150, 'FizzBuzz'),
        (13, '13'),
        (4, '4'),
        (31, '31'),
    ],
)
def test_fizzbuzz(entrance, expected) -> None:
    """Unittest for this function."""
    assert fizzbuzz(entrance) == expected
