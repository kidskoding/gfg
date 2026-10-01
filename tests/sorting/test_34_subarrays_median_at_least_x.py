import pytest
from helpers import load

count_median_at_least = load(
    "sorting.34_subarrays_median_at_least_x"
).count_median_at_least


@pytest.mark.parametrize(
    "arr, x, expected",
    [
        ([5, 2, 4, 1], 4, 7),
        ([3, 7, 2, 0, 1, 5], 10, 0),
        ([1, 2, 3], 2, 5),
        ([2, 1], 2, 2),  # even length uses the upper middle
        ([5, 5, 5], 5, 6),
        ([1], 1, 1),
        ([1], 2, 0),
        ([], 0, 0),
    ],
)
def test_count_median_at_least(arr, x, expected):
    assert count_median_at_least(arr, x) == expected
