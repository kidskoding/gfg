import pytest
from helpers import load

kth_missing_positive = load("10_searching.35_kth_missing_positive").kth_missing_positive


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([2, 3, 4, 7, 11], 5, 9),
        ([1, 2, 3], 2, 5),  # past the end
        ([3, 5, 9, 10, 11, 12], 2, 2),  # before the start
        ([5, 6, 7], 4, 4),
        ([1, 3], 1, 2),
        ([1], 1, 2),
        ([2], 1, 1),
        ([], 3, 3),
    ],
)
def test_kth_missing_positive(arr, k, expected):
    assert kth_missing_positive(arr, k) == expected
