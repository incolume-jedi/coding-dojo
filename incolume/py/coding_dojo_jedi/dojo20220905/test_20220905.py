from sys import version_info

import pytest
from dojo20220905 import stream


@pytest.mark.skipif(
    version_info < (3, 8, 0),
    reason='This run only Python 3.8+',
)
@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        ('deezer family', 34.9),
        ('Deezer Family', 34.9),
        ('Netflix padrão', 39.9),
        ('deezer free', 0.0),
        ('spotify free', 0.0),
        ('Disney Combo+', 45.90),
        ('Disney Disney+', 27.90),
        ('Disney starzplay', 55.90),
        ('netflix básico', 25.9),
        ('netflix premium', 55.9),
        ('Spotify Individual', 19.90),
        ('Spotify Duo', 24.90),
        ('Spotify Família', 34.90),
        ('Spotify Universitário', 9.90),
        ('deezer Family', 34.9),
        ('Deezer Premium', 19.9),
        ('Deezer HIFI', 34.9),
        ('Deezer Student', 9.9),
        ('Deezer Free', 0.0),
        ('disney starzplay', 55.9),
        ('disney free', 'Plano Indisponível'),
        ('foo free', 'Plano Indisponível'),
        ('netflix free', 'Plano Indisponível'),
    ),
)
def test_stream(entrance, expected):
    assert stream(entrance) == expected
