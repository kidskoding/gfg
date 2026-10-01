import pytest
from helpers import load

count_subarrays_max_in_range = load(
    "two_pointers.19_subarrays_max_in_range"
).count_subarrays_max_in_range


@pytest.mark.parametrize(
    "arr, left, right, expected",
    [
        ([2, 0, 11, 3, 0], 1, 10, 4),
        ([3, 4, 1], 2, 4, 5),
        ([2, 1, 4, 3], 2, 3, 3),
        ([-1, 2, -3], 0, 5, 4),
        ([5, 5, 5], 5, 5, 6),
        ([1, 1], 2, 3, 0),
        ([], 1, 2, 0),
    ],
)
def test_count_subarrays_max_in_range(arr, left, right, expected):
    assert count_subarrays_max_in_range(arr, left, right) == expected
