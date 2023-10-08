"""Tests examples."""
import sys
import unittest

import pytest

from incolume.py.coding_dojo_jedi.utils import check_connectivity

__author__ = '@britodfbr'  # pragma: no cover


class TestCaseExamplesDontRun:
    """This dont run."""

    __test__ = False

    def test_0(self) -> None:
        """Test it."""
        assert True

    def test_1(self) -> None:
        """Test it."""

    def test_2(self) -> None:
        """Test it."""


class TestCaseExamples:
    """Exemplos de testes para pytest."""

    @pytest.mark.skipif(
        not sys.platform.casefold().startswith('win'),
        reason='requires Windows',
    )
    def test_only_win(self) -> None:
        """Only windows."""
        # assert entrance in self.directories

    @pytest.mark.skipif(
        not sys.platform.casefold().startswith('mac'),
        reason='requires MacOS',
    )
    def test_only_mac(self) -> None:
        """Only mac."""

    @pytest.mark.skipif(
        not sys.platform.casefold().startswith('lin'),
        reason='requires Linux',
    )
    def test_only_lin(self) -> None:
        """Only linux."""

    @pytest.mark.xfail(reason='Proposital fail. expected "XFAIL"')
    def test_something_str(self) -> None:
        """Proposital fail. XFAIL."""
        assert 'a'.isdecimal() is True

    @pytest.mark.xfail(reason='Proposital fail. Expected "XPASS"')
    def test_something_digit(self) -> None:
        """Proposital fail. XPASS."""
        assert '1'.isdecimal() is True

    @pytest.mark.skip(reason='always skip.')
    def test_anything(self) -> None:
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
                    reason='proposital fail: expected XFAIL',
                ),
            ),
            pytest.param(
                'a',
                'a',
                marks=pytest.mark.xfail(
                    reason='proposital fail: expected XPASS',
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
    def test_something(self, entrance, expected) -> None:
        """Exemplo para multiplos testes."""
        assert entrance == expected


class MyTestCase(unittest.TestCase):
    """Exemplos com Unittest."""

    @classmethod
    def setUpClass(cls: object) -> None:
        """Pré-configuração da classe."""

    def setUp(self) -> None:
        """Preconfiguração para métodos."""

    @classmethod
    def tearDownClass(cls: object) -> None:
        """Método chamado imediatamente após concluir o método de teste."""
        #

    def tearDown(self) -> None:
        """Método chamado imediatamente após concluir a classe de teste."""
        #

    @unittest.skip('Futuring work')
    class MySkippedTestCase(unittest.TestCase):
        """Test case with skips."""

        def test_not_run(self) -> None:
            """Test not run."""

    @unittest.skipUnless(sys.platform.startswith('win'), 'requires Windows')
    def test_windows_support(self) -> None:
        """Windows specific testing code."""

    @unittest.skipUnless(sys.platform.startswith('mac'), 'requires MacOS')
    def test_mac_support(self) -> None:
        """MacOS specific testing code."""

    @unittest.skipUnless(sys.platform.startswith('lin'), 'requires Linux')
    def test_linux_support(self) -> None:
        """Linux specific testing code."""

    @unittest.skipUnless(
        check_connectivity(),
        reason='external resource not available',
    )
    def test_maybe_skipped(self) -> None:
        """Test code that depends on the external resource."""

    @unittest.skip('it never will run.')
    def test_something(self) -> None:
        """Este teste nunca irá passar.

        Defina um skip com a mensagem 'Dont ran'.
        """
        # pylint: disable=comparison-of-constants
        assert 'a'.isalpha() is False
