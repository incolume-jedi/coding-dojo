"""Test module."""

from __future__ import annotations
import inspect
import shutil
from typing import ClassVar, NoReturn
from collections.abc import Iterator
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
        <ol><li>
          <a href="http://legislacao.planalto.gov.br/legisla/legislacao.NSF/
Viw_Identificacao/ACP%2031-1966?OpenDocument"> Link </a>
          <a href="http://legislacao.planalto.gov.br/legisla/legislacao.Nsf/
Viw_Identificacao/ACP%2031-1966?OpenDocument"> Link </a>
          <a href="http://legislacao.planalto.gov.br/legisla/legislacao.nsf/
Viw_Identificacao/ACP%2031-1966?OpenDocument"> Link </a>
        </li><li>
          <a href="anexo/xpto.doc">anexo 1</a>
          <a href="anexo/xpto.Doc">anexo 2</a>
          <a href="anexo/xpto.DOC">anexo 3</a>
        </li><li>
          <a href="anexo/xpto.docx">anexo 4</a>
          <a href="anexo/xpto.Docx">anexo 5</a>
          <a href="anexo/xpto.DOCX">anexo 6</a>
        </li><li>
          <a href="anexo/xpto.xlsx">anexo 7</a>
          <a href="anexo/xpto.XLSX">anexo 8</a>
          <a href="anexo/xpto.Xlsx">anexo 9</a>
        </li><li>
          <a href="anexo/xpto.xls">anexo 10</a>
          <a href="anexo/xpto.Xls">anexo 11</a>
          <a href="anexo/xpto.XLS">anexo 12</a>
        </li><li>
        </li><li>
        </li><li>
          <a href="anexo/xpto.rtf">anexo 13</a>
          <a href="anexo/xpto.rtf">anexo 14</a>
          <a href="anexo/xpto.rtf">anexo 15</a>
        </li><li>
        </li><li>
        </li><li>
          <a href="anexo/xpto.pdf">anexo 16</a>
          <a href="anexo/xpto.Pdf">anexo 17</a>
          <a href="anexo/xpto.PDF">anexo 18</a>
        </li><li>
          <a href="D11923.htm">
            Decreto nº 11.923, de 22 de fev de 2024
          </a>
        </li><li>
          <a href="D11924.Htm">
            Decreto nº 11.924, de 22 de fev de 2024
          </a>
        </li><li>
          <a href="D11925.HTM">
            Decreto nº 11.925, de 22 de fev de 2024
          </a>
        </li><li>
          <a href="D11926.html">
            Decreto nº 11.926, de 22 de fev de 2024
          </a>
        </li><li>
          <a href="D11927.Html">
            Decreto nº 11.927, de 22 de fev de 2024
          </a>
        </li><li>
          <a href="D11928.htmL">
            Decreto nº 11.928, de 22 de fev de 2024
          </a>
        </li><li>
          <a href="D11929.HTML">
            Decreto nº 11.929, de 22 de fev de 2024
          </a>
        </li></ol>
      </body>
    </html>"""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                'doc',
                [
                    '<a href="anexo/xpto.doc">anexo 1</a>',
                    '<a href="anexo/xpto.Doc">anexo 2</a>',
                    '<a href="anexo/xpto.DOC">anexo 3</a>',
                    '<a href="anexo/xpto.docx">anexo 4</a>',
                    '<a href="anexo/xpto.Docx">anexo 5</a>',
                    '<a href="anexo/xpto.DOCX">anexo 6</a>',
                ],
                marks=[
                    # pytest.mark.skip,
                ],
            ),
            pytest.param(
                'docx',
                [
                    '<a href="anexo/xpto.docx">anexo 4</a>',
                    '<a href="anexo/xpto.Docx">anexo 5</a>',
                    '<a href="anexo/xpto.DOCX">anexo 6</a>',
                ],
                marks=[],
            ),
            pytest.param(
                'xlsx',
                [
                    '<a href="anexo/xpto.xlsx">anexo 7</a>',
                    '<a href="anexo/xpto.XLSX">anexo 8</a>',
                    '<a href="anexo/xpto.Xlsx">anexo 9</a>',
                ],
                marks=[],
            ),
            pytest.param(
                'xls',
                [
                    '<a href="anexo/xpto.xlsx">anexo 7</a>',
                    '<a href="anexo/xpto.XLSX">anexo 8</a>',
                    '<a href="anexo/xpto.Xlsx">anexo 9</a>',
                    '<a href="anexo/xpto.xls">anexo 10</a>',
                    '<a href="anexo/xpto.Xls">anexo 11</a>',
                    '<a href="anexo/xpto.XLS">anexo 12</a>',
                ],
                marks=[],
            ),
            pytest.param(
                'pdf',
                [
                    '<a href="anexo/xpto.pdf">anexo 16</a>',
                    '<a href="anexo/xpto.Pdf">anexo 17</a>',
                    '<a href="anexo/xpto.PDF">anexo 18</a>',
                ],
                marks=[],
            ),
            pytest.param(
                'rtf',
                [
                    '<a href="anexo/xpto.rtf">anexo 13</a>',
                    '<a href="anexo/xpto.rtf">anexo 14</a>',
                    '<a href="anexo/xpto.rtf">anexo 15</a>',
                ],
                marks=[],
            ),
            pytest.param(
                'nsf',
                [
                    '<a href="http://legislacao.planalto.gov.br/legisla/'
                    'legislacao.NSF/\nViw_Identificacao/ACP%2031-1966?'
                    'OpenDocument"> Link </a>',
                    '<a href="http://legislacao.planalto.gov.br/legisla/'
                    'legislacao.Nsf/\nViw_Identificacao/ACP%2031-1966?'
                    'OpenDocument"> Link </a>',
                    '<a href="http://legislacao.planalto.gov.br/legisla/'
                    'legislacao.nsf/\nViw_Identificacao/ACP%2031-1966?'
                    'OpenDocument"> Link </a>',
                ],
                marks=[],
            ),
            pytest.param(
                None,
                [
                    '<a href="anexo/xpto.doc">anexo 1</a>',
                    '<a href="anexo/xpto.Doc">anexo 2</a>',
                    '<a href="anexo/xpto.DOC">anexo 3</a>',
                    '<a href="anexo/xpto.docx">anexo 4</a>',
                    '<a href="anexo/xpto.Docx">anexo 5</a>',
                    '<a href="anexo/xpto.DOCX">anexo 6</a>',
                ],
                marks=[],
            ),
            pytest.param(
                '',
                [
                    '<a href="anexo/xpto.doc">anexo 1</a>',
                    '<a href="anexo/xpto.Doc">anexo 2</a>',
                    '<a href="anexo/xpto.DOC">anexo 3</a>',
                    '<a href="anexo/xpto.docx">anexo 4</a>',
                    '<a href="anexo/xpto.Docx">anexo 5</a>',
                    '<a href="anexo/xpto.DOCX">anexo 6</a>',
                ],
                marks=[],
            ),
        ],
    )
    def test_find_list_ahref_files(self, entrance, expected):
        """Unit test."""
        filein = utils.pseudo_filename()
        filein.write_text(self.content)
        soup = pkg.get_content_html(filein)
        assert [
            str(x) for x in pkg.find_list_ahref_files(soup, ext=entrance)
        ] == expected

    def test_find_list_ahref_files_0(self):
        """Unit test."""
        entrance = utils.pseudo_filename()
        expected = [
            '<a href="anexo/xpto.doc">anexo 1</a>',
            '<a href="anexo/xpto.docx">anexo 4</a>',
            '<a href="anexo/xpto.docx">anexo 4</a>',
            '<a href="anexo/xpto.rtf">anexo 13</a>',
            '<a href="anexo/xpto.rtf">anexo 14</a>',
            '<a href="anexo/xpto.rtf">anexo 15</a>',
            '<a href="anexo/xpto.xlsx">anexo 7</a>',
            '<a href="anexo/xpto.xls">anexo 10</a>',
            '<a href="anexo/xpto.xlsx">anexo 7</a>',
            '<a href="http://legislacao.planalto.gov.br/legisla/legislacao.nsf/'
            '\nViw_Identificacao/ACP%2031-1966?OpenDocument"> Link </a>',
        ]
        entrance.write_text(self.content)
        soup = pkg.get_content_html(entrance)
        assert [str(x) for x in pkg.find_list_ahref_files_0(soup)] == expected

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
        assert isinstance(result, Iterator)
        assert list(result) == []

    def test_get_list_html_0(self) -> NoReturn:
        """Unittest."""
        dout = Path(gettempdir()) / inspect.stack()[0][3]
        dout.mkdir(exist_ok=True)
        ic(dout)
        assert isinstance(pkg.get_list_html(dout), Iterator)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                'arquivo1.html',
                [
                    '<a href="http://legislacao.planalto.gov.br/legisla/'
                    'legislacao.NSF/\nViw_Identificacao/ACP%2031-1966?'
                    'OpenDocument"> Link </a>',
                    '<a href="http://legislacao.planalto.gov.br/legisla/'
                    'legislacao.Nsf/\nViw_Identificacao/ACP%2031-1966?'
                    'OpenDocument"> Link </a>',
                    '<a href="http://legislacao.planalto.gov.br/legisla/'
                    'legislacao.nsf/\nViw_Identificacao/ACP%2031-1966?'
                    'OpenDocument"> Link </a>',
                    '<a href="anexo/xpto.doc">anexo 1</a>',
                    '<a href="anexo/xpto.Doc">anexo 2</a>',
                    '<a href="anexo/xpto.DOC">anexo 3</a>',
                    '<a href="anexo/xpto.docx">anexo 4</a>',
                    '<a href="anexo/xpto.Docx">anexo 5</a>',
                    '<a href="anexo/xpto.DOCX">anexo 6</a>',
                    '<a href="anexo/xpto.xlsx">anexo 7</a>',
                    '<a href="anexo/xpto.XLSX">anexo 8</a>',
                    '<a href="anexo/xpto.Xlsx">anexo 9</a>',
                    '<a href="anexo/xpto.xls">anexo 10</a>',
                    '<a href="anexo/xpto.Xls">anexo 11</a>',
                    '<a href="anexo/xpto.XLS">anexo 12</a>',
                    '<a href="anexo/xpto.rtf">anexo 13</a>',
                    '<a href="anexo/xpto.rtf">anexo 14</a>',
                    '<a href="anexo/xpto.rtf">anexo 15</a>',
                    '<a href="anexo/xpto.pdf">anexo 16</a>',
                    '<a href="anexo/xpto.Pdf">anexo 17</a>',
                    '<a href="anexo/xpto.PDF">anexo 18</a>',
                    '<a href="D11923.htm">\n            '
                    'Decreto nº 11.923, de 22 de fev de 2024\n          </a>',
                    '<a href="D11924.Htm">\n            '
                    'Decreto nº 11.924, de 22 de fev de 2024\n          </a>',
                    '<a href="D11925.HTM">\n            '
                    'Decreto nº 11.925, de 22 de fev de 2024\n          </a>',
                    '<a href="D11926.html">\n            '
                    'Decreto nº 11.926, de 22 de fev de 2024\n          </a>',
                    '<a href="D11927.Html">\n            '
                    'Decreto nº 11.927, de 22 de fev de 2024\n          </a>',
                    '<a href="D11928.htmL">\n            '
                    'Decreto nº 11.928, de 22 de fev de 2024\n          </a>',
                    '<a href="D11929.HTML">\n            '
                    'Decreto nº 11.929, de 22 de fev de 2024\n          </a>',
                ],
                marks=[],
            ),
            pytest.param(
                'arquivo2.htm',
                [
                    '<a href="http://legislacao.planalto.gov.br/legisla/'
                    'legislacao.NSF/\nViw_Identificacao/ACP%2031-1966?'
                    'OpenDocument"> Link </a>',
                    '<a href="http://legislacao.planalto.gov.br/legisla/'
                    'legislacao.Nsf/\nViw_Identificacao/ACP%2031-1966?'
                    'OpenDocument"> Link </a>',
                    '<a href="http://legislacao.planalto.gov.br/legisla/'
                    'legislacao.nsf/\nViw_Identificacao/ACP%2031-1966?'
                    'OpenDocument"> Link </a>',
                    '<a href="anexo/xpto.doc">anexo 1</a>',
                    '<a href="anexo/xpto.Doc">anexo 2</a>',
                    '<a href="anexo/xpto.DOC">anexo 3</a>',
                    '<a href="anexo/xpto.docx">anexo 4</a>',
                    '<a href="anexo/xpto.Docx">anexo 5</a>',
                    '<a href="anexo/xpto.DOCX">anexo 6</a>',
                    '<a href="anexo/xpto.xlsx">anexo 7</a>',
                    '<a href="anexo/xpto.XLSX">anexo 8</a>',
                    '<a href="anexo/xpto.Xlsx">anexo 9</a>',
                    '<a href="anexo/xpto.xls">anexo 10</a>',
                    '<a href="anexo/xpto.Xls">anexo 11</a>',
                    '<a href="anexo/xpto.XLS">anexo 12</a>',
                    '<a href="anexo/xpto.rtf">anexo 13</a>',
                    '<a href="anexo/xpto.rtf">anexo 14</a>',
                    '<a href="anexo/xpto.rtf">anexo 15</a>',
                    '<a href="anexo/xpto.pdf">anexo 16</a>',
                    '<a href="anexo/xpto.Pdf">anexo 17</a>',
                    '<a href="anexo/xpto.PDF">anexo 18</a>',
                    '<a href="D11923.htm">\n            '
                    'Decreto nº 11.923, de 22 de fev de 2024\n          </a>',
                    '<a href="D11924.Htm">\n            '
                    'Decreto nº 11.924, de 22 de fev de 2024\n          </a>',
                    '<a href="D11925.HTM">\n            '
                    'Decreto nº 11.925, de 22 de fev de 2024\n          </a>',
                    '<a href="D11926.html">\n            '
                    'Decreto nº 11.926, de 22 de fev de 2024\n          </a>',
                    '<a href="D11927.Html">\n            '
                    'Decreto nº 11.927, de 22 de fev de 2024\n          </a>',
                    '<a href="D11928.htmL">\n            '
                    'Decreto nº 11.928, de 22 de fev de 2024\n          </a>',
                    '<a href="D11929.HTML">\n            '
                    'Decreto nº 11.929, de 22 de fev de 2024\n          </a>',
                ],
                marks=[],
            ),
            pytest.param(
                'arquivo3.htm',
                [
                    '<a href="http://legislacao.planalto.gov.br/legisla/'
                    'legislacao.NSF/\nViw_Identificacao/ACP%2031-1966?'
                    'OpenDocument"> Link </a>',
                    '<a href="http://legislacao.planalto.gov.br/legisla/'
                    'legislacao.Nsf/\nViw_Identificacao/ACP%2031-1966?'
                    'OpenDocument"> Link </a>',
                    '<a href="http://legislacao.planalto.gov.br/legisla/'
                    'legislacao.nsf/\nViw_Identificacao/ACP%2031-1966?'
                    'OpenDocument"> Link </a>',
                    '<a href="anexo/xpto.doc">anexo 1</a>',
                    '<a href="anexo/xpto.Doc">anexo 2</a>',
                    '<a href="anexo/xpto.DOC">anexo 3</a>',
                    '<a href="anexo/xpto.docx">anexo 4</a>',
                    '<a href="anexo/xpto.Docx">anexo 5</a>',
                    '<a href="anexo/xpto.DOCX">anexo 6</a>',
                    '<a href="anexo/xpto.xlsx">anexo 7</a>',
                    '<a href="anexo/xpto.XLSX">anexo 8</a>',
                    '<a href="anexo/xpto.Xlsx">anexo 9</a>',
                    '<a href="anexo/xpto.xls">anexo 10</a>',
                    '<a href="anexo/xpto.Xls">anexo 11</a>',
                    '<a href="anexo/xpto.XLS">anexo 12</a>',
                    '<a href="anexo/xpto.rtf">anexo 13</a>',
                    '<a href="anexo/xpto.rtf">anexo 14</a>',
                    '<a href="anexo/xpto.rtf">anexo 15</a>',
                    '<a href="anexo/xpto.pdf">anexo 16</a>',
                    '<a href="anexo/xpto.Pdf">anexo 17</a>',
                    '<a href="anexo/xpto.PDF">anexo 18</a>',
                    '<a href="D11923.htm">\n            '
                    'Decreto nº 11.923, de 22 de fev de 2024\n          </a>',
                    '<a href="D11924.Htm">\n            '
                    'Decreto nº 11.924, de 22 de fev de 2024\n          </a>',
                    '<a href="D11925.HTM">\n            '
                    'Decreto nº 11.925, de 22 de fev de 2024\n          </a>',
                    '<a href="D11926.html">\n            '
                    'Decreto nº 11.926, de 22 de fev de 2024\n          </a>',
                    '<a href="D11927.Html">\n            '
                    'Decreto nº 11.927, de 22 de fev de 2024\n          </a>',
                    '<a href="D11928.htmL">\n            '
                    'Decreto nº 11.928, de 22 de fev de 2024\n          </a>',
                    '<a href="D11929.HTML">\n            '
                    'Decreto nº 11.929, de 22 de fev de 2024\n          </a>',
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

        result = pkg.dojo0(path_dir=filename.parents[0])
        ic(result)

        assert all(isinstance(r, pkg.Item) for r in result)
        assert filename in [r.file for r in result]
        assert [str(i) for i in result[-1].items] == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param({}, [], marks=[pytest.mark.xpass, pytest.mark.skip]),
        ],
    )
    def test_dojo_solution(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(**entrance) == expected
