"""Test module."""

import inspect
import shutil
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20250102 as pkg
from bs4 import BeautifulSoup
import pytest
from incolume.py.coding_dojo_jedi import utils
from icecream import ic
from pathlib import Path
from tempfile import gettempdir


class TestCase:
    """Test case class."""

    t0: ClassVar = None
    content: ClassVar[str] = """
    <html>
      <body>
        <ol>
        <li>
          <a href="http://legislacao.planalto.gov.br/legisla/legislacao.nsf/
Viw_Identificacao/ACP%2031-1966?OpenDocument"> Link </a>
        </li>
        <li>
          <a href="anexo/xpto.doc">anexo 1</a>
        </li>
        <li>
          <a href="anexo/xpto.docx">anexo 2</a>
        </li>
        <li>
          <a href="anexo/xpto.xlsx">anexo 3</a>
        </li>
        <li>
          <a href="anexo/xpto.xls">anexo 4</a>
        </li>
        <li>
          <a href="anexo/xpto.rtf">anexo 5</a>
        </li>
        <li>
          <a href="anexo/xpto.pdf">anexo 6</a>
        </li>
        <li>
          <a href="D11927.htm">
            Decreto nº 11.927, de 22 de fev de 2024
          </a>
        </li>
        </ol>
      </body>
    </html>"""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                'arquivo1.html',
                [
                    '<a href="http://legislacao.planalto.gov.br/legisla/'
                    'legislacao.nsf/\nViw_Identificacao/ACP%2031-1966?'
                    'OpenDocument"> Link </a>',
                    '<a href="anexo/xpto.doc">anexo 1</a>',
                    '<a href="anexo/xpto.docx">anexo 2</a>',
                    '<a href="anexo/xpto.xlsx">anexo 3</a>',
                    '<a href="anexo/xpto.xls">anexo 4</a>',
                    '<a href="anexo/xpto.rtf">anexo 5</a>',
                    '<a href="anexo/xpto.pdf">anexo 6</a>',
                    '<a href="D11927.htm">\n            Decreto nº 11.927, de'
                    ' 22 de fev de 2024\n          </a>',
                ],
                marks=[],
            ),
            pytest.param(
                'arquivo2.htm',
                [
                    '<a href="http://legislacao.planalto.gov.br/legisla/'
                    'legislacao.nsf/\nViw_Identificacao/ACP%2031-1966?'
                    'OpenDocument"> Link </a>',
                    '<a href="anexo/xpto.doc">anexo 1</a>',
                    '<a href="anexo/xpto.docx">anexo 2</a>',
                    '<a href="anexo/xpto.xlsx">anexo 3</a>',
                    '<a href="anexo/xpto.xls">anexo 4</a>',
                    '<a href="anexo/xpto.rtf">anexo 5</a>',
                    '<a href="anexo/xpto.pdf">anexo 6</a>',
                    '<a href="D11927.htm">\n            Decreto nº 11.927,'
                    ' de 22 de fev de 2024\n          </a>',
                ],
                marks=[],
            ),
            pytest.param(
                'arquivo3.htm',
                [
                    '<a href="http://legislacao.planalto.gov.br/legisla/'
                    'legislacao.nsf/\nViw_Identificacao/ACP%2031-1966?'
                    'OpenDocument"> Link </a>',
                    '<a href="anexo/xpto.doc">anexo 1</a>',
                    '<a href="anexo/xpto.docx">anexo 2</a>',
                    '<a href="anexo/xpto.xlsx">anexo 3</a>',
                    '<a href="anexo/xpto.xls">anexo 4</a>',
                    '<a href="anexo/xpto.rtf">anexo 5</a>',
                    '<a href="anexo/xpto.pdf">anexo 6</a>',
                    '<a href="D11927.htm">\n            Decreto nº 11.927,'
                    ' de 22 de fev de 2024\n          </a>',
                ],
                marks=[],
            ),
        ],
    )
    def test_3(self, entrance, expected) -> NoReturn:
        """Unittest."""
        filename = (
            utils.pseudo_filename()
            .parents[0]
            .joinpath(
                inspect.stack()[0][3],
                entrance,
            )
        )
        filename.parent.mkdir(exist_ok=True)
        ic('>>>>', entrance, filename)
        filename.write_text(self.content)
        ic(filename)

        result = pkg.dojo(path_dir=filename.parents[0])
        ic(result)

        assert all(isinstance(r, pkg.Item) for r in result)
        assert filename in [r.file for r in result]
        assert [str(i) for i in result[-1].items] == expected

    def test_2(self) -> NoReturn:
        """Unittest."""
        soup = BeautifulSoup(self.content, 'html5lib')
        assert pkg.find_list_ahref(soup)

    def test_1(self) -> NoReturn:
        """Unittest."""
        fake_file = next(pkg.get_list_html(pkg.directory[0]))
        assert isinstance(pkg.get_content_html(fake_file), BeautifulSoup)

    def test_get_list_html_2(self) -> NoReturn:
        """Unittest."""
        total = 10
        dout = Path(gettempdir()) / inspect.stack()[0][3]
        shutil.rmtree(dout, ignore_errors=True)
        dout.mkdir(exist_ok=True)
        ic(dout)
        expected = []
        for x in range(total):
            fx = dout / f'file{x}.htm{"" if x % 2 else "l"}'
            fx.write_text('')
            expected.append(fx)
        ic(expected)

        result = list(pkg.get_list_html(dout))
        assert len(result) == total
        assert result == expected

    def test_get_list_html_1(self) -> NoReturn:
        """Unittest."""
        dout = Path(gettempdir()) / inspect.stack()[0][3]
        dout.mkdir(exist_ok=True)
        ic(dout)
        result = pkg.get_list_html(dout)
        assert isinstance(result, map)
        assert list(result) == []

    def test_get_list_html_0(self) -> NoReturn:
        """Unittest."""
        dout = Path(gettempdir()) / inspect.stack()[0][3]
        dout.mkdir(exist_ok=True)
        ic(dout)
        assert isinstance(pkg.get_list_html(dout), map)
