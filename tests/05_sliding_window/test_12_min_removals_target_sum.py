import pytest
from helpers import load

min_removals = load("05_sliding_window.12_min_removals_target_sum").min_removals


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([3, 4, 1, 3, 2], 5, 2),
        ([1, 1, 4, 2, 3], 5, 2),
        ([3, 2, 20, 1, 1, 3], 10, 5),  # mix of both ends
        ([1, 2, 3], 6, 3),  # remove everything
        ([1, 2, 3], 0, 0),
        ([2], 2, 1),
        ([5, 6, 7, 8, 9], 4, -1),
        ([1, 1], 3, -1),
    ],
)
def test_min_removals(arr, target, expected):
    assert min_removals(arr, target) == expected
