import pytest
from helpers import load

max_sum_at_most_x = load("sliding_window.06_max_sum_at_most_x").max_sum_at_most_x


@pytest.mark.parametrize(
    "arr, x, expected",
    [
        ([1, 2, 3, 4, 5], 11, 10),
        ([2, 4, 6, 8, 10], 7, 6),
        ([7, 1, 8, 2], 9, 9),
        ([1, 1, 1, 1], 10, 4),  # whole array fits
        ([3], 3, 3),  # exactly x
        ([5, 6], 4, 0),  # nothing fits
        ([], 5, 0),
    ],
)
def test_max_sum_at_most_x(arr, x, expected):
    assert max_sum_at_most_x(arr, x) == expected
