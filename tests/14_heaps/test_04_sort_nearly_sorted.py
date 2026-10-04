import pytest
from helpers import load

sort_nearly_sorted = load("14_heaps.04_sort_nearly_sorted").sort_nearly_sorted


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([6, 5, 3, 2, 8, 10, 9], 3, [2, 3, 5, 6, 8, 9, 10]),
        ([10, 9, 8, 7, 4, 70, 60, 50], 4, [4, 7, 8, 9, 10, 50, 60, 70]),
        ([2, 1, 3, 2], 1, [1, 2, 2, 3]),
        ([2, 1], 1, [1, 2]),
        ([1, 2, 3], 0, [1, 2, 3]),
        ([5, 5, 5], 1, [5, 5, 5]),
        ([], 0, []),
    ],
)
def test_sort_nearly_sorted(arr, k, expected):
    assert sort_nearly_sorted(arr, k) is None
    assert arr == expected
