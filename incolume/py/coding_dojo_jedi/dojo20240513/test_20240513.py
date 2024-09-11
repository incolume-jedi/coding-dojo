"""Module."""

from pathlib import Path
from urllib.error import URLError
import pytest

from incolume.py.coding_dojo_jedi.dojo20240513 import (
    pd,
    url,
    scrap,
    save_dataframe,
)
from tempfile import NamedTemporaryFile

__author__ = '@britodfbr'  # pragma: no cover


class CheckDojo:
    """Test case."""

    # @pytest.mark.skipif(
    #     raises=[URLError, TimeoutError],
    #     reason='URL conection error.',
    # )
    def test_raspagem_tabela_html(self):
        """Test scrap."""
        assert isinstance(scrap(url), pd.DataFrame)

    # @pytest.mark.skipif(
    #     raises=[URLError, TimeoutError],
    #     reason='URL conection error.',
    # )
    def test_raspagem_shape(self):
        """Test scrap."""
        assert scrap(url).shape == (258, 9)

    # @pytest.mark.skipif(
    #     raises=[URLError, TimeoutError],
    #     reason='URL conection error.',
    # )
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
        data = scrap(url)
        filename = Path(
            NamedTemporaryFile(
                prefix='testting-',
                suffix=f'.{format_output}',
            ).name,
        )
        result = save_dataframe(
            df=data,
            filename=filename,
            format_output=format_output,
        )
        assert result.is_file()
