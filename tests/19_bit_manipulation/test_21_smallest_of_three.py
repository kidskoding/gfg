import pytest
from helpers import load

smallest_of_three = load("19_bit_manipulation.21_smallest_of_three").smallest_of_three


@pytest.mark.parametrize(
    "x, y, z, expected",
    [
        (12, 15, 5, 5),
        (100, 7, 7, 7),
        (5, 5, 5, 5),
        (-3, 0, 3, -3),
        (0, -1, -1, -1),
        (2**40, -(2**40), 0, -(2**40)),
    ],
)
def test_smallest_of_three(x, y, z, expected):
    assert smallest_of_three(x, y, z) == expected
