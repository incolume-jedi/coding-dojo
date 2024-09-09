"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240915 as pkg
import pytest


class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'exception entrance expected'.split(),
        [
            pytest.param({}, None, True),
            pytest.param({}, '', True),
            pytest.param({}, ' ', True),
            pytest.param({}, '[]' * 52, True),
            pytest.param(
                {
                    'expected_exception': pkg.SizeError,
                    'match': r'count limit \d+\w*',
                },
                '[]' * 53,
                True,
            ),
            pytest.param({}, '()', True),
            pytest.param({}, r'()[]{}', True),
            pytest.param({}, r'{[()]()}', True),
            pytest.param({}, r'{[(]()}', False),
            pytest.param({}, '(]', False),
            pytest.param({}, '()[()]{[]}()]', False),
            pytest.param({}, '[0()[()]{[]}()]', True),
            pytest.param(
                {}, '[10e5(6+9)[3(1.73 - .73)+2]{2[3.5]**2}+(2-1)**3]', True,
            ),
        ],
    )
    def test_0(self, exception, entrance, expected) -> NoReturn:
        """Unittest."""
        if exception:
            with pytest.raises(**exception):
                pkg.dojo(entrance)
        else:
            assert pkg.dojo(entrance) == expected
