import pytest
from helpers import load

min_increments = load("sorting.20_min_increments_distinct").min_increments


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([3, 2, 1, 2, 1, 7], 6),
        ([1, 2, 2], 1),
        ([1, 1, 1, 1], 6),
        ([2, 2, 2, 1], 3),
        ([1, 2, 3], 0),
        ([5], 0),
        ([], 0),
    ],
)
def test_min_increments(arr, expected):
    assert min_increments(arr) == expected
