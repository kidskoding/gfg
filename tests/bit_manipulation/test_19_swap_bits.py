import pytest
from helpers import load

swap_bits = load("bit_manipulation.19_swap_bits").swap_bits


@pytest.mark.parametrize(
    "x, p1, p2, n, expected",
    [
        (47, 1, 5, 3, 227),
        (28, 0, 3, 2, 7),
        (15, 0, 4, 4, 240),
        (9, 0, 1, 1, 10),
        (5, 0, 2, 1, 5),  # both bits set: unchanged
        (1, 0, 1, 1, 2),
        (0, 0, 4, 4, 0),
    ],
)
def test_swap_bits(x, p1, p2, n, expected):
    assert swap_bits(x, p1, p2, n) == expected
