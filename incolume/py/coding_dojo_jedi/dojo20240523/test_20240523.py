"""Module."""

__author__ = '@britodfbr'  # pragma: no cover

from unittest import mock

from . import analise_nota


class Testcase:
    """Test case."""

    def test_quantidade(self, capsys):
        """Quantidade."""
        with mock.patch('builtins.input', side_effect=[7, 5, -1]):
            analise_nota()
            out, _ = capsys.readouterr()
        assert 'quantidade: 2;' in out

    def test_list(self, capsys):
        """Quantidade."""
        with mock.patch('builtins.input', side_effect=[7, 5, -1]):
            analise_nota()
            out, _ = capsys.readouterr()
        assert 'Notas: 7 5;' in out

    def test_rev(self, capsys):
        """Quantidade."""
        with mock.patch('builtins.input', side_effect=[7, 5, -1]):
            analise_nota()
            out, _ = capsys.readouterr()
        assert 'Reverso: 5 7;' in out

    def test_soma(self, capsys):
        """Quantidade."""
        with mock.patch('builtins.input', side_effect=[7, 5, -1]):
            analise_nota()
            out, _ = capsys.readouterr()
        assert 'Soma: 12;' in out

    def test_media(self, capsys):
        """Média."""
        with mock.patch('builtins.input', side_effect=[7, 5, -1]):
            analise_nota()
            out, _ = capsys.readouterr()
        assert 'Média: 6.0;' in out

    def test_acima_media(self, capsys):
        """Média acima."""
        with mock.patch('builtins.input', side_effect=[7, 5, -1]):
            analise_nota()
            out, _ = capsys.readouterr()
        assert 'Acima da média: 7;' in out

    def test_abaixo_sete(self, capsys):
        """Média acima."""
        with mock.patch('builtins.input', side_effect=[7, 5, -1]):
            analise_nota()
            out, _ = capsys.readouterr()
        assert 'Abaixo de 7: 5;' in out

    def test_msg_out(self, capsys):
        """Test dojo."""
        with mock.patch('builtins.input', side_effect=[7, 5, -1]):
            analise_nota()
            out, _ = capsys.readouterr()

            assert 'Bye bye.' in out
