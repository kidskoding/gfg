import pytest
from helpers import load

booth_multiply = load("19_bit_manipulation.44_booths_multiplication").booth_multiply


@pytest.mark.parametrize(
    "m, q, bits, expected",
    [
        (3, 4, 4, 12),
        (-5, 3, 4, -15),
        (7, -7, 4, -49),
        (-7, -7, 4, 49),
        (2, -3, 8, -6),
        (100, -100, 8, -10000),
        (1, 1, 2, 1),
        (0, 5, 4, 0),
    ],
)
def test_booth_multiply(m, q, bits, expected):
    assert booth_multiply(m, q, bits) == expected


def test_booth_multiply_exhaustive_5_bit():
    for m in range(-15, 16):
        for q in range(-15, 16):
            assert booth_multiply(m, q, 5) == m * q
