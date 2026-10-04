import pytest
from helpers import load

max_subarray_sum = load("01_arrays.23_max_subarray_sum").max_subarray_sum


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 3, -8, 7, -1, 2, 3], 11),
        ([-2, -4], -2),
        ([5, 4, 1, 7, 8], 25),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([-7], -7),
        ([0, -1, 0], 0),
    ],
)
def test_max_subarray_sum(arr, expected):
    assert max_subarray_sum(arr) == expected
