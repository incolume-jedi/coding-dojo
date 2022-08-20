import pytest
from dojo import classify


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    (
        ((4, [33, 37, 87, 87, 23]), ((87, 87, 37, 33), (23, 33, 37, 87))),
        ((7, [33, 37, 87, 87, 23, 83, 29, 85, 18, 28, 82, 93, 23, 16, 9]), ((93, 87, 87, 85, 83, 82, 37), (9, 16, 18, 23, 23, 28, 29))),
        ((1, [33, 37, 87, 87, 23]), (87, 23)),
        #((4, [33, 37, 87, 87, 23, 83, 29, 85, 18, 28, 82, 93, 23, 16, 9]), ((93, 87, 87, 85))(23, 23, 28, 29))),
    )
)

def test_classify(entrance, expected):
    assert classify(*entrance) == expected
