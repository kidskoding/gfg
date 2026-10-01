import pytest
from helpers import load

msb_number = load("bit_manipulation.16_most_significant_set_bit").msb_number


@pytest.mark.parametrize(
    "n, expected",
    [
        (10, 8),
        (18, 16),
        (32, 32),
        (255, 128),
        (1, 1),
        (2**40 + 5, 2**40),
        (0, 0),
    ],
)
def test_msb_number(n, expected):
    assert msb_number(n) == expected
