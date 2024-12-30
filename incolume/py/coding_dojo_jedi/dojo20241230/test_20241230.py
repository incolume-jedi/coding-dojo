"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241230 as pkg
from bs4 import BeautifulSoup


class TestCase:
    """Test case class."""

    t0: ClassVar = None
    content: ClassVar = """
    <html>
      <body>
        <p>
          <a href="anexo/xpto.doc">anexo 1</a>
          <a href="anexo/xpto.docx">anexo 2</a>
          <a href="anexo/xpto.xlsx">anexo 3</a>
          <a href="anexo/xpto.xls">anexo 4</a>
          <a href="anexo/xpto.rtf">anexo 5</a>
          <a href="anexo/xpto.pdf">anexo 6</a>
        </p><p>
          <a href="D11927.htm">
            Decreto nº 11.927, de 22 de fev de 2024
          </a>
        </p>
      </body>
    </html>"""

    def test_3(self) -> NoReturn:
        """Unittest."""
        assert pkg.dojo()

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
