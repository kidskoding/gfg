import pytest
from helpers import load

count_balanced_removals = load("01_arrays.37_equal_even_odd_sums").count_balanced_removals


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 1, 6, 4], 1),
        ([1, 1, 1], 3),
        ([1, 2, 3], 0),
        ([5], 1),
        ([1, 2], 0),
        ([0, 0, 0, 0], 4),
    ],
)
def test_count_balanced_removals(arr, expected):
    assert count_balanced_removals(arr) == expected
