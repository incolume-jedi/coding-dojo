import pytest

from incolume.py.coding_dojo_jedi.dojo20220812.dojo20220812 import tower


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    (
        (1, ['*']),
        (2, [' * ', '***']),
        (3, ['  *  ', ' *** ', '*****']),
        (
            6,
            [
                '     *     ',
                '    ***    ',
                '   *****   ',
                '  *******  ',
                ' ********* ',
                '***********',
            ],
        ),
        (
            11,
            [
                '          *          ',
                '         ***         ',
                '        *****        ',
                '       *******       ',
                '      *********      ',
                '     ***********     ',
                '    *************    ',
                '   ***************   ',
                '  *****************  ',
                ' ******************* ',
                '*********************',
            ],
        ),
        (
            20,
            [
                '                   *                   ',
                '                  ***                  ',
                '                 *****                 ',
                '                *******                ',
                '               *********               ',
                '              ***********              ',
                '             *************             ',
                '            ***************            ',
                '           *****************           ',
                '          *******************          ',
                '         *********************         ',
                '        ***********************        ',
                '       *************************       ',
                '      ***************************      ',
                '     *****************************     ',
                '    *******************************    ',
                '   *********************************   ',
                '  ***********************************  ',
                ' ************************************* ',
                '***************************************',
            ],
        ),
    ),
)
def test_tower(entrance, expected):
    assert tower(entrance) == expected