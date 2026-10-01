import pytest
from helpers import load

rightmost_set_bit_position = load(
    "bit_manipulation.17_rightmost_set_bit"
).rightmost_set_bit_position


@pytest.mark.parametrize(
    "n, expected",
    [
        (18, 2),
        (19, 1),
        (12, 3),
        (40, 4),
        (1, 1),
        (2**31, 32),
        (0, 0),
    ],
)
def test_rightmost_set_bit_position(n, expected):
    assert rightmost_set_bit_position(n) == expected
