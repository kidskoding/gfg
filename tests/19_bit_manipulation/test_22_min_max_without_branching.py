import pytest
from helpers import load

min_max = load("19_bit_manipulation.22_min_max_without_branching").min_max


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (15, 6, (6, 15)),
        (6, 15, (6, 15)),
        (-1, 1, (-1, 1)),
        (-10, -20, (-20, -10)),
        (7, 7, (7, 7)),
        (0, 2**31, (0, 2**31)),
    ],
)
def test_min_max(x, y, expected):
    assert min_max(x, y) == expected
