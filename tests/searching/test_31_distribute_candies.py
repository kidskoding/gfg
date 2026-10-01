import pytest
from helpers import load

distribute_candies = load("searching.31_distribute_candies").distribute_candies


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (10, 3, [5, 2, 3]),
        (7, 4, [1, 2, 3, 1]),  # last person gets the remainder
        (20, 3, [5, 7, 8]),
        (100, 4, [28, 27, 21, 24]),
        (10, 5, [1, 2, 3, 4, 0]),  # someone gets nothing
        (15, 1, [15]),
        (1, 1, [1]),
        (0, 3, [0, 0, 0]),
    ],
)
def test_distribute_candies(n, k, expected):
    assert distribute_candies(n, k) == expected
