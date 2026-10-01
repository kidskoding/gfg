import pytest
from helpers import load

transform_and_sort = load("arrays.34_transform_and_sort").transform_and_sort


@pytest.mark.parametrize(
    "arr, a, b, c, expected",
    [
        ([-4, -2, 2, 4], 1, 3, 5, [3, 9, 15, 33]),
        ([-4, -2, 2, 4], -1, 3, 5, [-23, -5, 1, 7]),
        ([-1, 0, 1, 2, 3, 4], -1, 2, -1, [-9, -4, -4, -1, -1, 0]),
        ([1, 2, 3], 0, 2, 0, [2, 4, 6]),
        ([1, 2, 3], 0, -2, 0, [-6, -4, -2]),
        ([5], 2, 0, 1, [51]),
        ([], 1, 1, 1, []),
    ],
)
def test_transform_and_sort(arr, a, b, c, expected):
    assert transform_and_sort(arr, a, b, c) == expected
