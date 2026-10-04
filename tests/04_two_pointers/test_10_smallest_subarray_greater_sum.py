import pytest
from helpers import load

smallest_subarray_with_sum = load(
    "04_two_pointers.10_smallest_subarray_greater_sum"
).smallest_subarray_with_sum


@pytest.mark.parametrize(
    "arr, x, expected",
    [
        ([1, 4, 45, 6, 0, 19], 51, 3),
        ([1, 10, 5, 2, 7], 9, 1),
        ([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280, 4),
        ([1, 1, 1, 1], 2, 3),
        ([1, 2, 4], 8, 0),
        ([5], 4, 1),
        ([5], 5, 0),  # must be strictly greater
        ([], 0, 0),
    ],
)
def test_smallest_subarray_with_sum(arr, x, expected):
    assert smallest_subarray_with_sum(arr, x) == expected
