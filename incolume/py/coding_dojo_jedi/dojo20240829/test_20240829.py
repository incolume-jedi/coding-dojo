"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240829 as pkg
import pytest
import sys


class TestCase:
    """Test case class."""

    def test_0(self) -> NoReturn:
        """Unittest."""
        entrance = (
            'Jesus Cristo',
            pkg.dt.datetime(1, 12, 25, 0, 0, 1),
            'Nazaré',
        )
        assert isinstance(pkg.Pessoa(*entrance), pkg.Pessoa)

    def test_1(self) -> NoReturn:
        """Unittest."""
        entrance = (
            'Jesus Cristo',
            pkg.dt.datetime(1, 12, 25, 0, 0, 1),
            'Nazaré',
        )
        expected = {
            'full_name': 'Jesus Cristo',
            'born_date': pkg.dt.datetime(1, 12, 25, 0, 0, 1),
            'city': 'Nazaré',
            'first_name': 'Jesus',
            'last_name': 'Cristo',
        }
        assert pkg.asdict(pkg.Pessoa(*entrance)) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                (
                    'Jesus Cristo',
                    pkg.dt.datetime(1, 12, 25, 0, 0, 1),
                    'Nazaré',
                ),
                'Meu nome é "Jesus" nascido em '
                '"Tuesday 25 de December do ano 1" na cidade de "Nazaré"',
                marks=[pytest.mark.skipif(not sys.platform.startswith("lin"),    reason="fork only available on Linux")]
            ),
            pytest.param(
                (
                    'Jesus Cristo',
                    pkg.dt.datetime(1, 12, 25, 0, 0, 1),
                    'Nazaré',
                ),
                'Meu nome é "Jesus" nascido em '
                '"Tuesday 25 de December do ano 0001" na cidade de "Nazaré"',
                marks=[pytest.mark.skipif(not sys.platform.startswith("mac"),    reason="fork only available on MacOS")]
            ),
            pytest.param(
                (
                    'Jesus Cristo',
                    pkg.dt.datetime(1, 12, 25, 0, 0, 1),
                    'Nazaré',
                ),
                'Meu nome é "Jesus" nascido em '
                '"Tuesday 25 de December do ano 1" na cidade de "Nazaré"',
                marks=[pytest.mark.skipif(not sys.platform.startswith("win"),    reason="fork only available on Windows")]
            ),
        ],
    )
    def test_2(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo0(pkg.Pessoa(*entrance)) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                (
                    'Jesus Cristo',
                    pkg.dt.datetime(1, 12, 25, 0, 0, 1),
                    'Nazaré',
                ),
                'Meu nome é "Jesus" nascido em '
                '"Tuesday 25 de December do ano 1" na cidade de "Nazaré"',
                marks=[pytest.mark.skipif(not sys.platform.startswith("lin"),    reason="fork only available on Linux")]
            ),
            pytest.param(
                (
                    'Jesus Cristo',
                    pkg.dt.datetime(1, 12, 25, 0, 0, 1),
                    'Nazaré',
                ),
                'Meu nome é "Jesus" nascido em '
                '"Tuesday 25 de December do ano 0001" na cidade de "Nazaré"',
                marks=[pytest.mark.skipif(not sys.platform.startswith("mac"),    reason="fork only available on MacOS")]
            ),
            pytest.param(
                (
                    'Jesus Cristo',
                    pkg.dt.datetime(1, 12, 25, 0, 0, 1),
                    'Nazaré',
                ),
                'Meu nome é "Jesus" nascido em '
                '"Tuesday 25 de December do ano 1" na cidade de "Nazaré"',
                marks=[pytest.mark.skipif(not sys.platform.startswith("win"),    reason="fork only available on Windows")]
            ),
        ],
    )
    def test_3(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(pkg.Pessoa(*entrance)) == expected
