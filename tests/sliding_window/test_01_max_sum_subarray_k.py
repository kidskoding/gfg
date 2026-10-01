import pytest
from helpers import load

max_sum_k = load("sliding_window.01_max_sum_subarray_k").max_sum_k


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([100, 200, 300, 400], 2, 700),
        ([1, 4, 2, 10, 23, 3, 1, 0, 20], 4, 39),
        ([5], 1, 5),
        ([-3, -1, -2], 2, -3),  # all negative
        ([1, 2, 3], 3, 6),  # k == len(arr)
        ([4, -1, 4, -1], 1, 4),
    ],
)
def test_max_sum_k(arr, k, expected):
    assert max_sum_k(arr, k) == expected
