import pytest
from helpers import load

sort_by_freq = load("09_sorting.19_sort_by_frequency").sort_by_freq


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([5, 5, 4, 6, 4], [4, 4, 5, 5, 6]),
        ([9, 9, 9, 2, 5], [9, 9, 9, 2, 5]),
        ([-1, 2, 2, -1, 3, 3, 3], [3, 3, 3, -1, -1, 2, 2]),
        ([3, 1, 2], [1, 2, 3]),
        ([3], [3]),
        ([], []),
    ],
)
def test_sort_by_freq(arr, expected):
    assert sort_by_freq(arr) == expected
