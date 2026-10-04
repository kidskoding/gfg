import pytest
from helpers import load

max_activities = load("17_greedy.01_activity_selection").max_activities


@pytest.mark.parametrize(
    "start, finish, expected",
    [
        ([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9], 4),
        (
            [10, 12, 20],
            [20, 25, 30],
            1,
        ),  # touching endpoints do not count as compatible
        ([1, 3, 2, 5], [2, 4, 3, 6], 3),
        ([1, 2, 3], [2, 3, 4], 2),  # chain of touching intervals
        ([5, 1, 3], [6, 2, 4], 3),  # unsorted, all disjoint
        ([1, 1, 1], [2, 2, 2], 1),  # all identical
        ([5], [7], 1),
        ([], [], 0),
    ],
)
def test_max_activities(start, finish, expected):
    assert max_activities(start, finish) == expected
