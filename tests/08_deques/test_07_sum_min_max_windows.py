import pytest
from helpers import load

sum_min_max_windows = load("08_deques.07_sum_min_max_windows").sum_min_max_windows


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([2, 5, -1, 7, -3, -1, -2], 4, 18),
        ([4, 1, 3, 2], 2, 14),
        ([1, 2, 3], 1, 12),
        ([1, 2, 3], 3, 4),
        ([5, 5, 5, 5], 2, 30),
        ([-1, -2], 2, -3),
        ([3], 1, 6),
        ([1, 2], 3, 0),
    ],
)
def test_sum_min_max_windows(arr, k, expected):
    assert sum_min_max_windows(arr, k) == expected
