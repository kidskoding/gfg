import pytest
from helpers import load

is_subset_sum = load("dynamic_programming.07_subset_sum").is_subset_sum


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([3, 34, 4, 12, 5, 2], 9, True),
        ([3, 34, 4, 12, 5, 2], 30, False),
        ([1, 2, 3], 6, True),
        ([2, 4, 6], 5, False),
        ([5], 0, True),
        ([5], 5, True),
        ([], 0, True),
        ([], 1, False),
    ],
)
def test_is_subset_sum(arr, target, expected):
    assert is_subset_sum(arr, target) == expected
