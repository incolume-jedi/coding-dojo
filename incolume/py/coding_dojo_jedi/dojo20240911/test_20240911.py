"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240911 as pkg
import pytest


class TestCase:
    """Test case class."""

    def test_0(self):
        """Unit test."""
        assert [(x.name, x.value) for x in pkg.Chess] == [
            ('vazio', 0),
            ('peão', 1),
            ('bispo', 2),
            ('cavalo', 3),
            ('torre', 4),
            ('dama', 5),
            ('rei', 6),
        ]

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            ('peão', pkg.Chess.peão),
            ('1', pkg.Chess.peão),
            (1, pkg.Chess.peão),
        ],
    )
    def test_1(self, entrance, expected) -> NoReturn:
        """Unit test."""
        assert pkg.Chess(entrance) == expected

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                [
                    ['0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '1', '1', '0', '0', '0'],
                    ['0', '0', '0', '1', '1', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0'],
                ],
                'Peão: 4 peças; ',
            ),
            pytest.param(
                [
                    ['4', '3', '2', '5', '6', '2', '3', '4'],
                    ['1', '1', '1', '1', '1', '1', '1', '1'],
                    ['0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0'],
                    ['0', '0', '0', '0', '0', '0', '0', '0'],
                    ['1', '1', '1', '1', '1', '1', '1', '1'],
                    ['4', '3', '2', '5', '6', '2', '3', '4'],
                ],
                'Torre: 4 peças; Cavalo: 4 peças; Bispo: 4 peças;'
                ' Dama: 2 peças; Rei: 2 peças; Peão: 16 peças; ',
                marks=[],
            ),
        ],
    )
    def test_2(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected
