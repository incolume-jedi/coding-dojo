"""Test module."""

import logging
import sys
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20240606 as pkg
import pytest


class TestCase:
    """Test case class."""

    case_test_square: ClassVar = [
        pytest.param(
            range(5),
            [pow(x, 2) for x in range(5)],
            marks=pytest.mark.skipif(
                condition=sys.platform.startswith('win'),
                reason='Not available on windows.',
            ),
        ),
    ]

    case_test_cube: ClassVar = [
        pytest.param(
            list(range(5)),
            [pow(x, 3) for x in range(5)],
            marks=pytest.mark.skipif(
                condition=sys.platform.startswith('win'),
                reason='Not available on windows.',
            ),
        ),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        case_test_square,
    )
    def test_square_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.calc_square0(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        case_test_cube,
    )
    def test_cube_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.calc_cube0(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        case_test_square,
    )
    def test_square_1(self, entrance, expected, caplog) -> NoReturn:
        """Unittest."""
        with caplog.at_level(logging.DEBUG):
            assert pkg.calc_square(entrance) == expected
            assert 'calc_square executou em' in caplog.text

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        case_test_cube,
    )
    def test_cube_1(self, entrance, expected, caplog) -> NoReturn:
        """Unittest."""
        with caplog.at_level(logging.DEBUG):
            assert pkg.calc_cube(entrance) == expected
            assert 'calc_cube executou em' in caplog.text
