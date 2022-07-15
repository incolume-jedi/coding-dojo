import pytest
import dojo


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    (
        ('Python', 'nohtyP'),
        ('Brasil', 'lisarB'),
        ('Ada', 'adA'),
        ('Ana', 'anA'),
    )
)
def test_rev(entrance, expected):
    assert dojo.rev(entrance) == expected
