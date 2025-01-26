"""Test module."""

from typing import ClassVar
import incolume.py.coding_dojo_jedi.dojo20250104 as pkg
import incolume.py.coding_dojo_jedi.dojo20250104.example_0 as ex0
import incolume.py.coding_dojo_jedi.dojo20250104.example_1 as ex1
import incolume.py.coding_dojo_jedi.dojo20250104.example_2 as ex2
import incolume.py.coding_dojo_jedi.dojo20250104.example_3 as ex3
import pytest
import tempfile
from pathlib import Path
import tarfile
import httpx
import respx
from http import HTTPStatus
from incolume.py.coding_dojo_jedi.utils import check_connectivity


class TestHandlerFiles:
    """Test case class."""

    t0: ClassVar = None
    expected_content: ClassVar[bytes] = b'3.1415926535'

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'url': pkg.URL_TAR_FILE,
                    'dir_output': Path(tempfile.gettempdir()),
                },
                'pi-1M.tar.gz',
                marks=[
                    pytest.mark.offci,
                    pytest.mark.webtest,
                    pytest.mark.xpass(
                        reason='failing web connection (but shoulded ran)',
                    ),
                    pytest.mark.skipif(
                        not check_connectivity(),
                        reason='failing web connection (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                {'dir_output': Path(tempfile.gettempdir())},
                'pi-1M.tar.gz',
                marks=[
                    pytest.mark.offci,
                    pytest.mark.webtest,
                    pytest.mark.xpass(
                        reason='failing web connection (but shoulded ran)',
                    ),
                    pytest.mark.skipif(
                        not check_connectivity(),
                        reason='failing web connection (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                {},
                'pi-1M.tar.gz',
                marks=[
                    pytest.mark.offci,
                    pytest.mark.webtest,
                    pytest.mark.xpass(
                        reason='failing web connection (but shoulded ran)',
                    ),
                    pytest.mark.skipif(
                        not check_connectivity(),
                        reason='failing web connection (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                {
                    'url': pkg.URL_RAW_FILE,
                    'fout': Path(tempfile.gettempdir()) / 'pi-1M.txt',
                },
                'pi-1M.txt',
                marks=[
                    pytest.mark.offci,
                    pytest.mark.webtest,
                    pytest.mark.xpass(
                        reason='failing web connection (but shoulded ran)',
                    ),
                    pytest.mark.skipif(
                        not check_connectivity(),
                        reason='failing web connection (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                {
                    'url': pkg.URL_TAR_FILE,
                    'fout': Path(tempfile.gettempdir()) / 'pi-1M.tgz',
                },
                'pi-1M.tgz',
                marks=[
                    pytest.mark.skip,
                    pytest.mark.offci,
                    pytest.mark.webtest,
                    pytest.mark.xpass(
                        reason='failing web connection (but shoulded ran)',
                    ),
                    pytest.mark.skipif(
                        not check_connectivity(),
                        reason='failing web connection (but shoulded ran)',
                    ),
                ],
            ),
        ],
    )
    def test_download(self, entrance, expected):
        """Unittest."""
        result = pkg.download_file(**entrance)
        assert expected in result.parts
        assert result.is_file()

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'dir_output': Path(tempfile.gettempdir())},
                'pi-1M.tar.gz',
                marks=[],
            ),
            pytest.param({}, 'pi-1M.tar.gz', marks=[]),
            pytest.param(
                {
                    'url': pkg.URL_RAW_FILE,
                    'fout': Path(tempfile.gettempdir()) / 'pi-1M.txt',
                },
                'pi-1M.txt',
                marks=[],
            ),
            pytest.param(
                {
                    'url': pkg.URL_RAW_FILE,
                    'fout': Path(*pkg.__package__.split('.')) / 'pi-1M.txt',
                },
                'pi-1M.txt',
                marks=[
                    # pytest.mark.skip
                ],
            ),
        ],
    )
    def test_download_mock_raw(self, entrance, expected):
        """Unittest."""
        fmock = (
            Path(*pkg.__package__.split('.')).parents[0]
            / 'generic_data/text_big/pi-1M.tgz'
        )
        with (
            respx.mock() as rmock,
            tarfile.open(
                fmock,
                mode='r:gz',
            ) as handler,
        ):
            file = handler.extractfile(handler.getnames()[0])
            content = file.read()
            test_route = rmock.get(entrance.get('url')).mock(
                return_value=httpx.Response(
                    HTTPStatus.OK,
                    content=content,
                ),
            )
            result = pkg.download_file(**entrance)
            assert test_route.called
            assert expected in result.parts
            assert result.is_file()

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'url': pkg.URL_TAR_FILE,
                    'dir_output': Path(tempfile.gettempdir()),
                },
                'pi-1M.tar.gz',
                marks=[],
            ),
            pytest.param(
                {'dir_output': Path(tempfile.gettempdir())},
                'pi-1M.tar.gz',
                marks=[],
            ),
            pytest.param({}, 'pi-1M.tar.gz', marks=[]),
            pytest.param(
                {
                    'url': pkg.URL_TAR_FILE,
                    'fout': Path(tempfile.gettempdir()) / 'pi-1M.tgz',
                },
                'pi-1M.tgz',
                marks=[
                    # pytest.mark.skip
                ],
            ),
        ],
    )
    def test_download_mock_tgz(self, entrance, expected):
        """Unittest."""
        fmock = pkg.LOCAL_FILE
        with respx.mock() as rmock:
            test_route = rmock.get(entrance.get('url')).mock(
                return_value=httpx.Response(
                    HTTPStatus.OK,
                    content=fmock.read_bytes(),
                ),
            )
            result = pkg.download_file(**entrance)
            assert test_route.called
            assert expected in result.parts
            assert result.is_file()

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {},
                b'3.14159265358979323846',
            ),
            pytest.param(
                {'fin': Path(tempfile.gettempdir()) / 'pi-1M.tar.gz'},
                b'3.14159265358979323846',
            ),
            pytest.param(
                {
                    'chunk': 101,
                    'fin': Path(tempfile.gettempdir()) / 'pi-1M.tar.gz',
                },
                b'3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798',
            ),
        ],
    )
    def test_handler_file(self, entrance, expected):
        """Unittest."""
        assert pkg.handler_file(**entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {},
                b'3.14159265358979323846',
            ),
            pytest.param(
                {
                    'chunk': 101,
                },
                b'3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798',
            ),
        ],
    )
    def test_handler_stream(self, entrance, expected):
        """Unittest."""
        fmock = pkg.LOCAL_FILE
        with (
            tarfile.open(fmock, mode='r:gz') as handler,
            respx.mock() as rmock,
        ):
            file = handler.extractfile(handler.getnames()[0])
            content = file.readline()

            test_route = rmock.get(entrance.get('url', pkg.URL_RAW_FILE)).mock(
                return_value=httpx.Response(
                    HTTPStatus.OK,
                    content=content,
                ),
            )

            assert pkg.handler_stream(**entrance) == expected
            assert test_route.called

    @pytest.mark.parametrize(
        'cmd entrance'.split(),
        [
            pytest.param(
                pkg.handler_file,
                {'chunk': 1.6180},
                marks=[pytest.mark.xpass(reason='bigger file.')],
            ),
            pytest.param(
                pkg.handler_file,
                {'chunk': 'a'},
                marks=[pytest.mark.xpass(reason='bigger file.')],
            ),
            pytest.param(
                pkg.handler_file,
                {'chunk': -1},
                marks=[pytest.mark.xpass(reason='bigger file.')],
            ),
        ],
    )
    def test_handler_bigger_mock(self, cmd, entrance):
        """Unittest."""
        with tarfile.open(
            pkg.LOCAL_FILE,
            mode='r:gz',
        ) as handler:
            file = handler.extractfile(handler.getnames()[0])
            expected = file.readline()
            result = cmd(**entrance).strip()

            assert result == expected

    @pytest.mark.parametrize(
        'cmd entrance'.split(),
        [
            pytest.param(
                pkg.handler_stream,
                {'chunk': 1.6180},
                marks=[pytest.mark.xpass(reason='bigger file.')],
            ),
            pytest.param(
                pkg.handler_stream,
                {'chunk': '1k'},
                marks=[pytest.mark.xpass(reason='bigger file.')],
            ),
            pytest.param(
                pkg.handler_stream,
                {'chunk': -1},
                marks=[pytest.mark.xpass(reason='bigger file.')],
            ),
        ],
    )
    def test_handler_bigger_mock_raw(self, cmd, entrance):
        """Unittest."""
        with (
            tarfile.open(
                pkg.LOCAL_FILE,
                mode='r:gz',
            ) as handler,
            respx.mock() as mresp,
        ):
            file = handler.extractfile(handler.getnames()[0])
            expected = file.readline()

            test_route = mresp.get(entrance.get('url', pkg.URL_RAW_FILE)).mock(
                return_value=httpx.Response(
                    HTTPStatus.OK,
                    content=expected,
                ),
            )

            result = cmd(**entrance).strip()
            assert test_route.called
            assert result == expected

    @pytest.mark.parametrize(
        'seq entrance expected'.split(),
        [
            pytest.param(1, {}, [b'1']),
            pytest.param(1, {'fin': pkg.LOCAL_FILE}, [b'1']),
            pytest.param(
                1,
                {'fin': pkg.LOCAL_FILE.with_suffix('.txt')},
                [b'1'],
                marks=[
                    # pytest.mark.skip
                ],
            ),
            pytest.param(
                20,
                {},
                [
                    b'1',
                    b'4',
                    b'1',
                    b'5',
                    b'9',
                    b'2',
                    b'6',
                    b'5',
                    b'3',
                    b'5',
                    b'8',
                    b'9',
                    b'7',
                    b'9',
                    b'3',
                    b'2',
                    b'3',
                    b'8',
                    b'4',
                    b'6',
                ],
            ),
            pytest.param(
                101,
                {},
                [
                    b'1',
                    b'4',
                    b'1',
                    b'5',
                    b'9',
                    b'2',
                    b'6',
                    b'5',
                    b'3',
                    b'5',
                    b'8',
                    b'9',
                    b'7',
                    b'9',
                    b'3',
                    b'2',
                    b'3',
                    b'8',
                    b'4',
                    b'6',
                    b'2',
                    b'6',
                    b'4',
                    b'3',
                    b'3',
                    b'8',
                    b'3',
                    b'2',
                    b'7',
                    b'9',
                    b'5',
                    b'0',
                    b'2',
                    b'8',
                    b'8',
                    b'4',
                    b'1',
                    b'9',
                    b'7',
                    b'1',
                    b'6',
                    b'9',
                    b'3',
                    b'9',
                    b'9',
                    b'3',
                    b'7',
                    b'5',
                    b'1',
                    b'0',
                    b'5',
                    b'8',
                    b'2',
                    b'0',
                    b'9',
                    b'7',
                    b'4',
                    b'9',
                    b'4',
                    b'4',
                    b'5',
                    b'9',
                    b'2',
                    b'3',
                    b'0',
                    b'7',
                    b'8',
                    b'1',
                    b'6',
                    b'4',
                    b'0',
                    b'6',
                    b'2',
                    b'8',
                    b'6',
                    b'2',
                    b'0',
                    b'8',
                    b'9',
                    b'9',
                    b'8',
                    b'6',
                    b'2',
                    b'8',
                    b'0',
                    b'3',
                    b'4',
                    b'8',
                    b'2',
                    b'5',
                    b'3',
                    b'4',
                    b'2',
                    b'1',
                    b'1',
                    b'7',
                    b'0',
                    b'6',
                    b'7',
                    b'9',
                    b'8',
                ],
            ),
        ],
    )
    def test_iterator(self, seq, entrance, expected):
        """Unittest."""
        it = pkg.iterator_handler_file(**entrance)
        assert [next(it) for _ in range(seq)] == expected


class TestPrimes:
    """Case teste."""

    test0: ClassVar = [
        ('2', False),
        ('2i', False),
        (b'2', False),
        (2.0, False),
    ]
    test1: ClassVar = [
        (10**5, False),
        (9323, True),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (41, True),
        (59, True),
        (89, True),
    ]
    test2: ClassVar[list[int]] = [
        997,
        991,
        983,
        977,
        971,
        967,
        953,
        947,
        941,
        937,
        929,
        919,
        911,
        907,
        887,
        883,
        881,
        877,
        863,
        859,
        857,
        853,
        839,
        829,
        827,
        823,
        821,
        811,
        809,
        797,
        787,
        773,
        769,
        761,
        757,
        751,
        743,
        739,
        733,
        727,
        719,
        709,
        701,
        691,
        683,
        677,
        673,
        661,
        659,
        653,
        647,
        643,
        641,
        631,
        619,
        617,
        613,
        607,
        601,
        599,
        593,
        587,
        577,
        571,
        569,
        563,
        557,
        547,
        541,
        523,
        521,
        509,
        503,
        499,
        491,
        487,
        479,
        467,
        463,
        461,
        457,
        449,
        443,
        439,
        433,
        431,
        421,
        419,
        409,
        401,
        397,
        389,
        383,
        379,
        373,
        367,
        359,
        353,
        349,
        347,
        337,
        331,
        317,
        313,
        311,
        307,
        293,
        283,
        281,
        277,
        271,
        269,
        263,
        257,
        251,
        241,
        239,
        233,
        229,
        227,
        223,
        211,
        199,
        197,
        193,
        191,
        181,
        179,
        173,
        167,
        163,
        157,
        151,
        149,
        139,
        137,
        131,
        127,
        113,
        109,
        107,
        103,
        101,
        97,
        89,
        83,
        79,
        73,
        71,
        67,
        61,
        59,
        53,
        47,
        43,
        41,
        37,
        31,
        29,
        23,
        19,
        17,
        13,
        11,
        7,
        5,
        3,
        2,
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test0 + test1,
    )
    def test_is_prime(self, entrance, expected):
        """Check is prime number."""
        assert pkg.is_prime(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test1,
    )
    def test_is_prime_ex0(self, entrance, expected):
        """Check is prime number."""
        obj = ex0.PrimesPi(pkg.LOCAL_FILE)
        assert obj.is_prime(entrance) == expected

    @pytest.mark.parametrize(
        'funct expected'.split(),
        [
            pytest.param(pkg.is_prime, test2, marks=[]),
            pytest.param(ex0.PrimesPi('').is_prime, test2, marks=[]),
        ],
    )
    def test_sequence0(self, funct, expected):
        """Unititest."""
        primes = [x for x in range(10**3, -1, -1) if funct(x)]
        assert primes == expected

    @pytest.mark.parametrize(
        'funct expected'.split(),
        [
            pytest.param(ex2.get_prime, test2, marks=[]),
            pytest.param(ex3.get_prime, test2, marks=[]),
        ],
    )
    def test_sequence1(self, funct, expected):
        """Unititest."""
        primes = list(reversed(funct(10**3)))
        assert primes == expected


class TestCaseExamples:
    """Case Examples."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                pkg.LOCAL_FILE.with_suffix('.txt'),
                '14590431451723416161791510706177671741511297009743626357169179809791310760755',
                marks=[
                    pytest.mark.offci,
                    pytest.mark.slow,
                ],
            ),
        ],
    )
    def test_example_0(self, entrance, expected):
        """Example case."""
        prime_finder = ex0.PrimesPi(
            filename=entrance,
        )
        result = prime_finder.run()
        assert result == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                pkg.LOCAL_FILE.with_suffix('.tar.gz'),
                1,
                marks=[
                    pytest.mark.offci,
                    pytest.mark.slow,
                ],
            ),
        ],
    )
    def test_example_0_xcpt(self, entrance, expected):
        """Example case."""
        prime_finder = ex0.PrimesPi(
            filename=entrance,
        )
        with pytest.raises(SystemExit) as excinfo:  # noqa: PT012
            prime_finder.run()
            assert excinfo.value.code == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                pkg.LOCAL_FILE.with_suffix('.txt'),
                '14590431451723416161791510706177671741511297009743626357169179809791310760755',
                marks=[
                    pytest.mark.offci,
                    pytest.mark.slow,
                ],
            ),
        ],
    )
    def test_example_1(self, entrance, expected):
        """Example case."""
        assert ex1.ic_biggest_seq(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'prime_array': ex2.get_prime(10**4),
                    'array': ex2.load_file(
                        pkg.LOCAL_FILE.with_suffix('.txt').open(),
                    ),
                    'begin': 1,
                    'sequence': '',
                    'bigger_sequence': None,
                },
                ['4159265358979323'],
                marks=[pytest.mark.offci, pytest.mark.slow],
            ),
        ],
    )
    def test_example_2(self, entrance, expected):
        """Example case."""
        result = ['']
        entrance.update({'bigger_sequence': result})
        ex2.generate_bigger_primes(**entrance)
        assert result == expected

    def test_example_3(self):
        """Example case."""
        expected = ['4159265358979323']
        result = ['']
        primes = ex3.get_prime(10000)
        ex3.get_bigger_seq(
            prime_array=primes,
            array=ex3.load_file(pkg.LOCAL_FILE.with_suffix('.txt').open()),
            begin=1,
            seq='',
            bigger_seq=result,
        )
        assert result == expected


class TestPrimesIntoPI:
    """Case teste."""

    __test__ = False

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'begin': 1, 'seq': '1415926535'},
                '',
                marks=[pytest.mark.xpass],
            ),
            pytest.param(
                {'begin': 1, 'seq': '14159265358979323846'},
                '',
                marks=[pytest.mark.xpass],
            ),
        ],
    )
    def test_find_longest_prime_sequence(self, entrance, expected):
        """Unittest."""
        assert pkg.find_longest_prime_sequence(**entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'chunk': 4, 'fin': pkg.LOCAL_FILE},
                '41 59 2 653 5 89 7 9323',
                marks=[
                    pytest.mark.skip,
                ],
            ),
            pytest.param(
                {'chunk': 4, 'fin': pkg.LOCAL_FILE.with_suffix('.txt')},
                '41 59 2 653 5 89 7 9323',
                marks=[
                    pytest.mark.skip,
                ],
            ),
            pytest.param({'chunk': 20}, '41 59 2 653 5 89 7 9323'),
        ],
    )
    def test_seq(self, entrance, expected):
        """Unittest."""
        assert pkg.dojo(**entrance) == expected
