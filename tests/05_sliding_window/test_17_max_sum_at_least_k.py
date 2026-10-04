import pytest
from helpers import load

max_sum_at_least_k = load("05_sliding_window.17_max_sum_at_least_k").max_sum_at_least_k


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([-4, -2, 1, -3], 2, -1),
        ([1, 1, 1, 1, 1, 1], 2, 6),
        ([1, -10, 5, 6], 2, 11),
        ([5, 7, -9, 3, -4, 2, 1, -8, 9, 10], 5, 16),
        ([2, -1, 3], 3, 4),  # whole array forced
        ([-1, -2, -3], 1, -1),
        ([5], 1, 5),
    ],
)
def test_max_sum_at_least_k(arr, k, expected):
    assert max_sum_at_least_k(arr, k) == expected
