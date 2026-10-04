import pytest
from helpers import load

sum_min_abs_diff = load("09_sorting.03_sum_min_abs_difference").sum_min_abs_diff


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([4, 1, 5], 5),
        ([5, 10, 1, 4, 8, 7], 9),
        ([1, 1], 0),
        ([-3, 2], 10),
        ([-1, -5, 3, 10], 19),
        ([2, 2, 2, 7], 5),
    ],
)
def test_sum_min_abs_diff(arr, expected):
    assert sum_min_abs_diff(arr) == expected
