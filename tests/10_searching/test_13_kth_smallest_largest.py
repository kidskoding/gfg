import pytest
from helpers import load

kth_smallest = load("10_searching.13_kth_smallest_largest").kth_smallest
kth_largest = load("10_searching.13_kth_smallest_largest").kth_largest


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([7, 10, 4, 3, 20, 15], 3, 7),
        ([7, 10, 4, 3, 20, 15], 4, 10),
        ([7, 10, 4, 20, 15], 4, 15),
        ([2, 1, 2, 1], 3, 2),  # duplicates counted
        ([5, 5, 5], 2, 5),
        ([-1, -5, 3], 1, -5),
        ([1], 1, 1),
    ],
)
def test_kth_smallest(arr, k, expected):
    assert kth_smallest(arr, k) == expected


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([7, 10, 4, 3, 20, 15], 3, 10),
        ([1, 23, 12, 9, 30, 2, 50], 3, 23),
        ([12, 3, 5, 7, 19], 2, 12),
        ([5, 5, 4], 2, 5),  # duplicates counted
        ([-1, -5, 3], 3, -5),
        ([1], 1, 1),
    ],
)
def test_kth_largest(arr, k, expected):
    assert kth_largest(arr, k) == expected
