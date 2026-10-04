import pytest
from helpers import load

floor_index = load("10_searching.05_floor_in_sorted_array").floor_index

ARR = [1, 2, 8, 10, 10, 12, 19]


@pytest.mark.parametrize(
    "arr, x, expected",
    [
        (ARR, 0, -1),
        (ARR, 5, 1),
        (ARR, 10, 4),  # last occurrence of the floor
        (ARR, 20, 6),
        (ARR, 1, 0),
        ([2, 2, 2], 3, 2),
        ([5], 5, 0),
        ([5], 4, -1),
        ([], 1, -1),
    ],
)
def test_floor_index(arr, x, expected):
    assert floor_index(arr, x) == expected
