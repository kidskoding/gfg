import pytest
from helpers import load

merge_intervals = load("09_sorting.11_merge_overlapping_intervals").merge_intervals


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[1, 3], [2, 4], [6, 8], [9, 10]], [[1, 4], [6, 8], [9, 10]]),
        ([[7, 8], [1, 5], [2, 4], [4, 6]], [[1, 6], [7, 8]]),
        ([[1, 4], [4, 5]], [[1, 5]]),  # touching intervals merge
        ([[1, 10], [2, 3], [4, 5]], [[1, 10]]),
        ([[3, 4], [1, 2]], [[1, 2], [3, 4]]),
        ([[5, 5]], [[5, 5]]),
        ([], []),
    ],
)
def test_merge_intervals(intervals, expected):
    assert merge_intervals(intervals) == expected
