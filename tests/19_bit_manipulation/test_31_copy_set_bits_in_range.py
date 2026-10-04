import pytest
from helpers import load

copy_set_bits = load("19_bit_manipulation.31_copy_set_bits_in_range").copy_set_bits


@pytest.mark.parametrize(
    "x, y, l, r, expected",
    [
        (10, 13, 2, 3, 14),
        (8, 7, 1, 2, 11),
        (0, 255, 3, 4, 12),
        (0, 255, 1, 8, 255),
        (16, 31, 1, 32, 31),
        (5, 2, 1, 1, 5),  # y has nothing set in range
        (0, 0, 1, 5, 0),
    ],
)
def test_copy_set_bits(x, y, l, r, expected):
    assert copy_set_bits(x, y, l, r) == expected
