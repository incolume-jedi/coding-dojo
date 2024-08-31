"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240831 as pkg
import pytest


class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                [
                    'ate',
                    'eta',
                    'eat',
                    'bat',
                    'tab',
                    'nat',
                    'tan',
                    'ant',
                    'tea',
                ],
                [
                    ['ant', 'nat', 'tan'],
                    ['ate', 'eat', 'eta', 'tea'],
                    ['bat', 'tab'],
                ],
            ),
            (
                [
                    'bad',
                    'cbda',
                    'dbac',
                    'dba',
                    'adb',
                    'dbca',
                    'bcad',
                    'dcab',
                    'dcba',
                    'cabd',
                    'cadb',
                    'bda',
                    'bad',
                    'abd',
                    'acbd',
                    'bcda',
                    'cbad',
                    'dabc',
                    'adbc',
                    'bdca',
                    'cdab',
                    'abdc',
                    'dacb',
                    'adcb',
                ],
                [
                    ['abd', 'adb', 'bad', 'bad', 'bda', 'dba'],
                    [
                        'abdc',
                        'acbd',
                        'adbc',
                        'adcb',
                        'bcad',
                        'bcda',
                        'bdca',
                        'cabd',
                        'cadb',
                        'cbad',
                        'cbda',
                        'cdab',
                        'dabc',
                        'dacb',
                        'dbac',
                        'dbca',
                        'dcab',
                        'dcba',
                    ],
                ],
            ),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.group_anagram(entrance) == expected

    def test_1(self):
        """Unut test."""
        entrance = 'ab'
        expected = ['ab', 'ba']
        assert all(item in expected for item in pkg.anagrams_gen(entrance))
