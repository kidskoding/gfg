import pytest
from helpers import load

sum_of_subarrays = load("01_arrays.18_sum_of_all_subarrays").sum_of_subarrays


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3], 20),
        ([1, 4, 5, 3, 2], 116),
        ([5], 5),
        ([], 0),
        ([-1, 2], 2),
        ([1, 1, 1, 1], 20),
    ],
)
def test_sum_of_subarrays(arr, expected):
    assert sum_of_subarrays(arr) == expected
