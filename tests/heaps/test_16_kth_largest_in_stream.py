import pytest
from helpers import load

kth_largest_in_stream = load("heaps.16_kth_largest_in_stream").kth_largest_in_stream


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 2, 3, 4, 5, 6], 4, [-1, -1, -1, 1, 2, 3]),
        ([10, 20, 11, 70, 50, 40, 100, 5], 3, [-1, -1, 10, 11, 20, 40, 50, 50]),
        ([3, 4], 1, [3, 4]),
        ([3, 1, 2], 1, [3, 3, 3]),
        ([5, 5, 5], 2, [-1, 5, 5]),
        ([], 1, []),
    ],
)
def test_kth_largest_in_stream(arr, k, expected):
    assert kth_largest_in_stream(arr, k) == expected
