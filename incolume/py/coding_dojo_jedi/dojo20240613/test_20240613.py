"""Test module."""

from pathlib import Path
from typing import NoReturn
from unittest import mock

import pandas as pd

import incolume.py.coding_dojo_jedi.dojo20240613 as pkg
import pytest
from tempfile import NamedTemporaryFile


class TestCase:
    """Test case class."""

    @pytest.mark.skip()
    def test_0(self) -> NoReturn:
        """Unittest."""
        expected = (
            'Nicolas Silva Silva',
            '630.418.957-57',
            'nicolas-sampaio-barros@correios.com.br',
        )
        with mock.patch(pkg.fake, return_value=mock.MagicMock()) as m:
            m.last_name.return_value = 'Silva'
            m.fake.cpf.return_value = expected[1]
            m.fake.slug.return_value = 'nicolas-silva-silva'
            assert pkg.data_fake() == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (15, (15, 3)),
            (None, (10, 3)),
        ],
    )
    def test_1(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.generate_dataframe(entrance).shape == expected

    @pytest.mark.parametrize(
        'entrance',
        [
            {
                'filename': Path(NamedTemporaryFile().name),
                'data': pkg.generate_dataframe(),
            },
            {
                'data': pkg.generate_dataframe(),
            },
        ],
    )
    def test_2(self, entrance) -> NoReturn:
        """Unittest."""
        assert pkg.write_xlsx(**entrance)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                {
                    'k': 3,
                    'filename': Path(NamedTemporaryFile(suffix='.xlsx').name),
                },
                3,
            ),
            (
                {
                    'k': 10,
                    'filename': Path(NamedTemporaryFile(suffix='.xlsx').name),
                },
                10,
            ),
        ],
    )
    def test_3(self, entrance, expected) -> NoReturn:
        """Unittest."""
        pkg.write_xlsx(
            data=pkg.generate_dataframe(100),
            filename=entrance.get('filename'),
        )
        result = pkg.sorteio(**entrance)
        assert pd.read_excel(result).shape[0] == expected
