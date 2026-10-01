import pytest
from helpers import load

closest_to_zero_sum = load("searching.21_sum_closest_to_zero").closest_to_zero_sum


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([-8, 5, 2, -6], -1),
        ([0, -8, -6, 3], 3),  # -3 and 3 tie: larger wins
        ([-3, 1, 5], 2),  # -2 and 2 tie
        ([-21, -67, -37, -18, 4, -65], -14),
        ([-5, 5, -4, 4], 0),
        ([-1, 3, -2], 1),
        ([2, -3], -1),
        ([1, 2], 3),  # all positive
    ],
)
def test_closest_to_zero_sum(arr, expected):
    assert closest_to_zero_sum(arr) == expected
