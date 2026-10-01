import pytest
from helpers import load

turn_off_rightmost_set_bit = load(
    "bit_manipulation.02_turn_off_rightmost_set_bit"
).turn_off_rightmost_set_bit


@pytest.mark.parametrize(
    "n, expected",
    [
        (12, 8),
        (7, 6),
        (10, 8),
        (255, 254),
        (8, 0),
        (1, 0),
        (0, 0),
    ],
)
def test_turn_off_rightmost_set_bit(n, expected):
    assert turn_off_rightmost_set_bit(n) == expected
