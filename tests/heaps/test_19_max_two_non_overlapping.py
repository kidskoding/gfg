import pytest
from helpers import load

max_two_non_overlapping = load(
    "heaps.19_max_two_non_overlapping"
).max_two_non_overlapping


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([(1, 3, 2), (4, 5, 2), (2, 4, 3)], 4),
        ([(1, 3, 2), (4, 5, 2), (1, 5, 5)], 5),  # one interval beats any pair
        ([(1, 10, 5), (2, 3, 4), (5, 6, 4), (7, 8, 4)], 8),
        ([(5, 6, 1), (1, 2, 1), (3, 4, 10)], 11),  # unsorted input
        ([(1, 2, 3), (2, 3, 4)], 4),  # sharing an endpoint overlaps
        ([(1, 2, 3), (3, 4, 4)], 7),
        ([(1, 1, 7)], 7),
        ([], 0),
    ],
)
def test_max_two_non_overlapping(intervals, expected):
    assert max_two_non_overlapping(intervals) == expected
