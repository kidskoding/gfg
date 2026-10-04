import pytest
from helpers import load

minimize_max_adjacent_diff = load(
    "08_deques.11_minimize_max_adjacent_diff"
).minimize_max_adjacent_diff


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([3, 7, 8, 10, 14], 2, 2),
        ([12, 16, 22, 31, 31, 38], 3, 6),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 1),
        ([1, 10, 11, 12, 30], 2, 1),
        ([-5, -3, 0, 4], 1, 3),
        ([1, 2, 10, 11], 2, 1),  # two left: best adjacent pair
        ([5, 5, 5, 5], 1, 0),
        ([1, 4, 6], 0, 3),  # nothing removed
    ],
)
def test_minimize_max_adjacent_diff(arr, k, expected):
    assert minimize_max_adjacent_diff(arr, k) == expected
