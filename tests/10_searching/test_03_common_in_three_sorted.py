import pytest
from helpers import load

common_in_three = load("10_searching.03_common_in_three_sorted").common_in_three


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (
            [1, 5, 10, 20, 40, 80],
            [6, 7, 20, 80, 100],
            [3, 4, 15, 20, 30, 70, 80, 120],
            [20, 80],
        ),
        ([1, 5, 5], [3, 4, 5, 5, 10], [5, 5, 10, 20], [5]),  # duplicates reported once
        ([1, 2, 3], [4, 5], [6], []),
        ([], [1], [1], []),
        ([1, 1, 1], [1, 1], [1], [1]),
        ([-3, -1, 0, 2], [-3, 0, 2, 4], [-5, -3, 0, 2], [-3, 0, 2]),
        ([1, 2], [1, 2], [2], [2]),
    ],
)
def test_common_in_three(a, b, c, expected):
    assert common_in_three(a, b, c) == expected
