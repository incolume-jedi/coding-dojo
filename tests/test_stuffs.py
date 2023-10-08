"""Tests examples."""
import sys
import unittest

import pytest

from incolume.py.coding_dojo_jedi.utils import check_connectivity

__author__ = '@britodfbr'  # pragma: no cover


class TestCaseExamplesDontRun:
    """This dont run."""

    __test__ = False

    def test_0(self):
        """Test it."""
        assert True

    def test_1(self):
        """Test it."""

    def test_2(self):
        """Test it."""


class TestCaseExamples:
    """Exemplos de testes para pytest."""

    @pytest.mark.skipif(
        not sys.platform.casefold().startswith('win'),
        reason='requires Windows',
    )
    def test_only_win(self):
        """Only windows."""
        # assert entrance in self.directories

    @pytest.mark.skipif(
        not sys.platform.casefold().startswith('mac'), reason='requires MacOS'
    )
    def test_only_mac(self):
        """Only mac."""

    @pytest.mark.skipif(
        not sys.platform.casefold().startswith('lin'), reason='requires Linux'
    )
    def test_only_lin(self):
        """Only linux."""

    @pytest.mark.xfail(reason='Proposital fail. expected "XFAIL"')
    def test_something_str(self):
        """Proposital fail. XFAIL."""
        assert 'a'.isdecimal() is True

    @pytest.mark.xfail(reason='Proposital fail. Expected "XPASS"')
    def test_something_digit(self):
        """Proposital fail. XPASS."""
        assert '1'.isdecimal() is True

    @pytest.mark.skip(reason='always skip.')
    def test_anything(self):
        """Always skip."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('', ''),
            pytest.param('a', 'a'),
            pytest.param(
                'a',
                '',
                marks=pytest.mark.xfail(
                    reason='proposital fail: expected XFAIL'
                ),
            ),
            pytest.param(
                'a',
                'a',
                marks=pytest.mark.xfail(
                    reason='proposital fail: expected XPASS'
                ),
            ),
            pytest.param('', '', marks=pytest.mark.skip(reason='skip')),
            pytest.param(
                '',
                '',
                marks=pytest.mark.skipif(
                    not sys.platform.casefold().startswith('mac'),
                    reason='requires MacOS',
                ),
            ),
            pytest.param(
                '',
                '',
                marks=pytest.mark.skipif(
                    not sys.platform.casefold().startswith('win'),
                    reason='requires Windows',
                ),
            ),
            pytest.param(
                '',
                '',
                marks=pytest.mark.skipif(
                    not sys.platform.casefold().startswith('lin'),
                    reason='requires Linux',
                ),
            ),
            pytest.param(
                '',
                '',
                marks=[
                    pytest.mark.skipif(
                        not sys.platform.casefold().startswith('mac'),
                        reason='requires MacOS',
                    ),
                    pytest.mark.xfail(reason='XPASS'),
                ],
            ),
            pytest.param(
                '',
                '',
                marks=[
                    pytest.mark.skipif(
                        not sys.platform.casefold().startswith('win'),
                        reason='requires Windows',
                    ),
                    pytest.mark.xfail(reason='XPASS'),
                ],
            ),
            pytest.param(
                '',
                '',
                marks=[
                    pytest.mark.skipif(
                        not sys.platform.casefold().startswith('lin'),
                        reason='requires Linux',
                    ),
                    pytest.mark.xfail(reason='XPASS'),
                ],
            ),
            pytest.param(
                '',
                '',
                marks=pytest.mark.skipif(
                    not check_connectivity(),
                    reason='external resource not available',
                ),
            ),
        ],
    )
    def test_something(self, entrance, expected):
        """Exemplo para multiplos testes."""
        assert entrance == expected


class MyTestCase(unittest.TestCase):
    """Exemplos com Unittest."""

    @classmethod
    def setUpClass(cls) -> None:
        # Pré-configuração da classe
        ...

    def setUp(self) -> None:
        # Preconfiguração para métodos
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        # Método chamado imediatamente após concluir o método de teste
        pass

    def tearDown(self) -> None:
        # Método chamado imediatamente após concluir a classe de teste
        pass

    @unittest.skip('Futuring work')
    class MySkippedTestCase(unittest.TestCase):
        def test_not_run(self):
            pass

    @unittest.skipUnless(sys.platform.startswith('win'), 'requires Windows')
    def test_windows_support(self):
        """Windows specific testing code."""

    @unittest.skipUnless(sys.platform.startswith('mac'), 'requires MacOS')
    def test_mac_support(self):
        """MacOS specific testing code."""

    @unittest.skipUnless(sys.platform.startswith('lin'), 'requires Linux')
    def test_linux_support(self):
        """Linux specific testing code."""

    @unittest.skipUnless(
        check_connectivity(), reason='external resource not available'
    )
    def test_maybe_skipped(self):
        """Test code that depends on the external resource."""

    @unittest.skip('it never will run.')
    def test_something(self):
        """Este teste nunca irá passar.

        Defina um skip com a mensagem 'Dont ran'.
        """
        # pylint: disable=comparison-of-constants
        assert True is False
