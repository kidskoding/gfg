import pytest
from helpers import load

kth_largest_subarray_sum = load(
    "heaps.20_kth_largest_sum_subarray"
).kth_largest_subarray_sum


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([20, -5, -1], 3, 14),
        ([10, -10, 20, -40], 6, -10),
        ([1, 2, 3], 1, 6),
        ([1, 2, 3], 4, 3),  # sums 6, 5, 3, 3, 2, 1
        ([1, 2, 3], 6, 1),
        ([2, 2, 2], 2, 4),
        ([5], 1, 5),
    ],
)
def test_kth_largest_subarray_sum(arr, k, expected):
    assert kth_largest_subarray_sum(arr, k) == expected
