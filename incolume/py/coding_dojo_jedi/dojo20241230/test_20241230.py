"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241230 as pkg
from bs4 import BeautifulSoup
import pytest
from incolume.py.coding_dojo_jedi import utils
from icecream import ic
import regex


class TestCase:
    """Test case class."""

    t0: ClassVar = None
    content: ClassVar[str] = """
    <html>
      <body>
        <p>
          <a href="http://legislacao.planalto.gov.br/legisla/legislacao.nsf/Viw_Identificacao/ACP%2031-1966?OpenDocument"> Link </a>
        </p>
        <p>
          <a href="anexo/xpto.doc">anexo 1</a>
          <a href="anexo/xpto.docx">anexo 2</a>
          <a href="anexo/xpto.xlsx">anexo 3</a>
          <a href="anexo/xpto.xls">anexo 4</a>
          <a href="anexo/xpto.rtf">anexo 5</a>
          <a href="anexo/xpto.pdf">anexo 6</a>
        </p>
        <p>
          <a href="D11927.htm">
            Decreto nº 11.927, de 22 de fev de 2024
          </a>
        </p>
      </body>
    </html>"""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                'arquivo1.html',
                regex.escape('[]'),
                marks=[],
            ),
            pytest.param('arquivo2.htm', '', marks=[pytest.mark.skip]),
            pytest.param('arquivo3.htm', '', marks=[pytest.mark.skip]),
        ],
    )
    def test_3(self, entrance, expected) -> NoReturn:
        """Unittest."""
        filename = utils.pseudo_filename().with_name(entrance)
        filename.write_text(self.content)
        ic(filename)
        assert (pkg.dojo(path_dir=filename.parents[0])) == expected

    def test_2(self) -> NoReturn:
        """Unittest."""
        soup = BeautifulSoup(self.content, 'html5lib')
        assert pkg.find_list_ahref(soup)

    def test_1(self) -> NoReturn:
        """Unittest."""
        fake_file = next(pkg.get_list_html(pkg.directory[0]))
        assert isinstance(pkg.get_content_html(fake_file), BeautifulSoup)

    def test_0(self) -> NoReturn:
        """Unittest."""
        assert isinstance(pkg.get_list_html(pkg.directory[0]), map)
