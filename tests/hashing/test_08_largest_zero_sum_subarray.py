import pytest
from helpers import load

max_len_zero_sum = load("hashing.08_largest_zero_sum_subarray").max_len_zero_sum


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([15, -2, 2, -8, 1, 7, 10, 23], 5),
        ([2, 10, 4], 0),
        ([1, 0, -4, 3, 1, 0], 5),
        ([1, -1], 2),  # whole array
        ([0], 1),
        ([0, 0, 0], 3),
        ([], 0),
        ([3, 4, -7, 3, 1, 3, 1, -4, -2, -2], 10),
    ],
)
def test_max_len_zero_sum(arr, expected):
    assert max_len_zero_sum(arr) == expected
