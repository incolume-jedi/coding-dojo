"""Module."""

from pathlib import Path
from unittest import mock
from incolume.py.coding_dojo_jedi.utils import genfile
import pytest

from incolume.py.coding_dojo_jedi.dojo20240513 import (
    pd,
    url,
    scrap,
    save_dataframe,
)

__author__ = '@britodfbr'  # pragma: no cover

file = Path(__file__).parent / 'Voltagem-codigos-2020-10-05.html'


class CheckDojo:
    """Test case."""

    dataframe = pd.read_html(file.read_bytes())

    def test_raspagem_tabela_html(self):
        """Test scrap."""
        with mock.patch('pandas.read_html', return_value=self.dataframe):
            assert isinstance(scrap(url), pd.DataFrame)

    def test_raspagem_shape(self):
        """Test scrap."""
        with mock.patch('pandas.read_html', return_value=self.dataframe):
            assert scrap(url).shape == (258, 9)

    @pytest.mark.parametrize(
        'format_output',
        [
            'csv',
            'json',
            'xlsx',
        ],
    )
    def test_output(self, format_output):
        """Test arquivo gravado."""
        with (
            mock.patch('pandas.read_html', return_value=self.dataframe),
        ):
            data = scrap(url)
            filename = genfile(prefix='testting-', suffix=f'.{format_output}')
            result = save_dataframe(
                df=data,
                filename=filename,
                format_output=format_output,
            )
            assert result.is_file()
