import pytest
from helpers import load

kth_smallest_in_ranges = load(
    "searching.24_kth_smallest_in_ranges"
).kth_smallest_in_ranges


@pytest.mark.parametrize(
    "ranges, queries, expected",
    [
        ([[1, 4], [6, 8]], [2, 6, 10], [2, 7, -1]),
        ([[2, 6], [5, 7]], [5, 8], [6, -1]),  # overlap counted once
        ([[5, 10], [1, 3]], [3, 4, 9, 10], [3, 5, 10, -1]),  # unsorted ranges
        ([[1, 10], [2, 3], [4, 5]], [10, 11], [10, -1]),  # nested ranges
        ([[1, 5], [6, 8]], [6], [6]),  # touching ranges
        ([[-3, -1], [0, 0]], [1, 4], [-3, 0]),
        ([[1, 1]], [1, 2], [1, -1]),
        ([], [1], [-1]),
    ],
)
def test_kth_smallest_in_ranges(ranges, queries, expected):
    assert kth_smallest_in_ranges(ranges, queries) == expected
