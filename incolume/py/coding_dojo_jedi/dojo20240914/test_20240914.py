"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240914 as pkg
import pytest


class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'exception entrance expected'.split(),
        [
            (
                {
                    'expected_exception': TypeError,
                    'match': 'only numbers between 2 to 9.',
                },
                9512,
                [],
            ),
            (
                {
                    'expected_exception': TypeError,
                    'match': 'only numbers between 2 to 9.',
                },
                9022,
                [],
            ),
            (
                {
                    'expected_exception': ValueError,
                    'match': r'`num` max \d+ digits.',
                },
                22222,
                [],
            ),
            (
                {
                    'expected_exception': TypeError,
                    'match': 'only numbers between 2 to 9.',
                },
                '9022',
                [],
            ),
            (
                {
                    'expected_exception': TypeError,
                    'match': 'only numbers between 2 to 9.',
                },
                'a',
                [],
            ),
            (
                {
                    'expected_exception': TypeError,
                    'match': 'only numbers between 2 to 9.',
                },
                '0',
                [],
            ),
            (
                {
                    'expected_exception': TypeError,
                    'match': 'only numbers between 2 to 9.',
                },
                ' ',
                [],
            ),
            pytest.param(
                {},
                '',
                [],
                marks=[],
            ),
            pytest.param({}, None, [], marks=[]),
            pytest.param(
                {
                    'expected_exception': TypeError,
                    'match': 'only numbers between 2 to 9.',
                },
                0,
                [],
                marks=[],
            ),
            pytest.param(None, '2', ['a', 'b', 'c'], marks=[]),
            pytest.param(
                None,
                '23',
                ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'],
                marks=[],
            ),
            pytest.param(
                None,
                '239',
                [
                    'adw',
                    'adx',
                    'ady',
                    'adz',
                    'aew',
                    'aex',
                    'aey',
                    'aez',
                    'afw',
                    'afx',
                    'afy',
                    'afz',
                    'bdw',
                    'bdx',
                    'bdy',
                    'bdz',
                    'bew',
                    'bex',
                    'bey',
                    'bez',
                    'bfw',
                    'bfx',
                    'bfy',
                    'bfz',
                    'cdw',
                    'cdx',
                    'cdy',
                    'cdz',
                    'cew',
                    'cex',
                    'cey',
                    'cez',
                    'cfw',
                    'cfx',
                    'cfy',
                    'cfz',
                ],
                marks=[],
            ),
            pytest.param(
                None,
                '2379',
                [
                    'adpw',
                    'adpx',
                    'adpy',
                    'adpz',
                    'adqw',
                    'adqx',
                    'adqy',
                    'adqz',
                    'adrw',
                    'adrx',
                    'adry',
                    'adrz',
                    'adsw',
                    'adsx',
                    'adsy',
                    'adsz',
                    'aepw',
                    'aepx',
                    'aepy',
                    'aepz',
                    'aeqw',
                    'aeqx',
                    'aeqy',
                    'aeqz',
                    'aerw',
                    'aerx',
                    'aery',
                    'aerz',
                    'aesw',
                    'aesx',
                    'aesy',
                    'aesz',
                    'afpw',
                    'afpx',
                    'afpy',
                    'afpz',
                    'afqw',
                    'afqx',
                    'afqy',
                    'afqz',
                    'afrw',
                    'afrx',
                    'afry',
                    'afrz',
                    'afsw',
                    'afsx',
                    'afsy',
                    'afsz',
                    'bdpw',
                    'bdpx',
                    'bdpy',
                    'bdpz',
                    'bdqw',
                    'bdqx',
                    'bdqy',
                    'bdqz',
                    'bdrw',
                    'bdrx',
                    'bdry',
                    'bdrz',
                    'bdsw',
                    'bdsx',
                    'bdsy',
                    'bdsz',
                    'bepw',
                    'bepx',
                    'bepy',
                    'bepz',
                    'beqw',
                    'beqx',
                    'beqy',
                    'beqz',
                    'berw',
                    'berx',
                    'bery',
                    'berz',
                    'besw',
                    'besx',
                    'besy',
                    'besz',
                    'bfpw',
                    'bfpx',
                    'bfpy',
                    'bfpz',
                    'bfqw',
                    'bfqx',
                    'bfqy',
                    'bfqz',
                    'bfrw',
                    'bfrx',
                    'bfry',
                    'bfrz',
                    'bfsw',
                    'bfsx',
                    'bfsy',
                    'bfsz',
                    'cdpw',
                    'cdpx',
                    'cdpy',
                    'cdpz',
                    'cdqw',
                    'cdqx',
                    'cdqy',
                    'cdqz',
                    'cdrw',
                    'cdrx',
                    'cdry',
                    'cdrz',
                    'cdsw',
                    'cdsx',
                    'cdsy',
                    'cdsz',
                    'cepw',
                    'cepx',
                    'cepy',
                    'cepz',
                    'ceqw',
                    'ceqx',
                    'ceqy',
                    'ceqz',
                    'cerw',
                    'cerx',
                    'cery',
                    'cerz',
                    'cesw',
                    'cesx',
                    'cesy',
                    'cesz',
                    'cfpw',
                    'cfpx',
                    'cfpy',
                    'cfpz',
                    'cfqw',
                    'cfqx',
                    'cfqy',
                    'cfqz',
                    'cfrw',
                    'cfrx',
                    'cfry',
                    'cfrz',
                    'cfsw',
                    'cfsx',
                    'cfsy',
                    'cfsz',
                ],
                marks=[],
            ),
        ],
    )
    def test_0(self, exception, entrance, expected) -> NoReturn:
        """Unittest."""
        if exception:
            with pytest.raises(**exception):
                pkg.dojo(entrance)
        else:
            assert pkg.dojo(entrance) == expected
