"""Test for dojo 20220811."""
# tests.py
import re
import sys
import unittest

import pytest
import requests

from incolume.py.coding_dojo_jedi.dojo20220811.dojo20220811 import calculadora


def check_connectivity(url: str = 'https://google.com') -> bool:
    """Check web connectivity."""
    try:
        req = requests.get(url, timeout=0.8)
        if req.status_code != 200:
            msg = 'Not connected'
            raise ConnectionError(msg)
        return True
    except ConnectionError:
        return False


@unittest.skip('Futuring work')
class MySkippedTestCase(unittest.TestCase):
    """Class MySkippedTestCase."""
    def test_not_run(self) -> None:
        """Test not run."""


class MyTestCase(unittest.TestCase):
    """Class MyTestCase."""
    @classmethod
    def setUpClass(cls) -> None:
        """Pré-configuração da classe."""

    def setUp(self) -> None:
        """Preconfiguração para métodos."""

    @classmethod
    def tearDownClass(cls) -> None:
        """Método chamado imediatamente após concluir o método de teste."""

    def tearDown(self) -> None:
        """Método chamado imediatamente após concluir a classe de teste."""

    @unittest.skipUnless(
        sys.platform.startswith('win'),
        'requires Windows',
    )
    def test_windows_support(self) -> None:
        """Windows specific testing code."""

    @unittest.skipUnless(
        sys.platform.startswith('mac'), 'requires MacOS')
    def test_mac_support(self) -> None:
        """MacOS specific testing code."""

    @unittest.skipUnless(
        sys.platform.startswith('lin'), 'requires Linux')
    def test_linux_support(self) -> None:
        """Linux specific testing code."""

    def test_maybe_skipped(self) -> None:
        """Test code that depends on the external resource."""
        if not check_connectivity():
            self.skipTest('external resource not available')

    @unittest.skip('it never will run.')
    def test_something(self) -> None:
        """Este teste nunca irá passar.

        Defina um skip com a mensagem 'Dont ran'.
        """
        # pylint: disable=comparison-of-constants
        assert True is False

class TestCalculadora(unittest.TestCase):
    """Test case calculadora."""

    def test_soma(self) -> None:
        """Test soma."""
        assert calculadora('+', 3, '4') == 7

    def test_soma_float(self) -> None:
        """Test soma float."""
        assert calculadora('+', 3, 4) == 7.0

    def test_menos(self) -> None:
        """Test menos."""
        assert calculadora('-', '3', 4) == -1

    def test_menos_float(self) -> None:
        """Test menos float."""
        assert calculadora('-', 3.0, 4) == -1.0

    def test_mult(self) -> None:
        """Test mult."""
        assert calculadora('*', 3, '4') == 12

    def test_mult_float(self) -> None:
        """Test mult float."""
        assert calculadora('*', 3, '4.0') == 12.0

    def test_dividir(self) -> None:
        """Test dividir inteiro."""
        assert calculadora('/', 3, '4') == 0.75

    def test_dividir_float(self) -> None:
        """Test dividir float."""
        assert calculadora('/', 4, 4.0) == 1.0
        assert calculadora('/', 4, 3) == 1.3333333333333333

    def test_mod(self) -> None:
        """Test mod."""
        assert calculadora('%', 4, 3) == 1
        assert calculadora('%', 12, 7) == 5

    def test_pow(self) -> None:
        """Test pow."""
        assert calculadora('**', 3, 4) == 81

    def test_dividir_except(self) -> None:
        """Test dividir except."""
        with pytest.raises(ValueError, match=r'.*y deve ser diferente de 0.*'):
            calculadora('/', 3, 0)
            calculadora('//', 3, 0)
            calculadora('//', 3, '0')

    def test_operador(self) -> None:
        """Test oprador."""
        with pytest.raises(
            ValueError,
            match=re.escape('Operador inválido. Use: +, -, *, **, //, /, %'),
        ):
            calculadora('^', 3, 5)

    def test_numeric_values(self) -> None:
        """Test numeric values."""
        with pytest.raises(
            ValueError,
            match='x e y devem ser valores numéricos reais.',
        ):
            calculadora('+', 'a', 'b')
            calculadora('+', '0', 'b')
            calculadora('+', 'a', '0')


if __name__ == '__main__':
    unittest.main()
