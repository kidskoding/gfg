import pytest
from helpers import load

square = load("19_bit_manipulation.29_square_without_multiply").square


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, 25),
        (12, 144),
        (1000, 1000000),
        (2**20, 2**40),
        (-7, 49),
        (-1, 1),
        (1, 1),
        (0, 0),
    ],
)
def test_square(n, expected):
    assert square(n) == expected
