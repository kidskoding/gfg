import pytest
from helpers import load

swap_numbers = load("bit_manipulation.14_swap_two_numbers").swap_numbers


@pytest.mark.parametrize(
    "a, b",
    [
        (10, 5),
        (5, 10),
        (-3, 7),
        (7, 7),
        (0, 9),
        (0, 0),
        (2**40, -1),
    ],
)
def test_swap_numbers(a, b):
    assert swap_numbers(a, b) == (b, a)
