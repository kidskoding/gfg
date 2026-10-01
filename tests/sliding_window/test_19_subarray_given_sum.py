import pytest
from helpers import load

subarray_with_sum = load("sliding_window.19_subarray_given_sum").subarray_with_sum


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 2, 3, 7, 5], 12, (1, 3)),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15, (0, 4)),
        ([1, 0, 0, 2], 2, (1, 3)),  # smallest end, then smallest start
        ([0, 3], 3, (0, 1)),  # leading zero kept: smallest start
        ([2, 0, 0], 2, (0, 0)),
        ([3, 0, 1], 0, (1, 1)),  # target 0 needs a non-empty zero run
        ([5, 3, 4], 2, None),
        ([], 1, None),
    ],
)
def test_subarray_with_sum(arr, target, expected):
    assert subarray_with_sum(arr, target) == expected
