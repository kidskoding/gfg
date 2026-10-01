import pytest
from helpers import load

max_meetings = load("sorting.17_max_meetings_one_room").max_meetings


@pytest.mark.parametrize(
    "start, end, expected",
    [
        ([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9], 4),
        ([10, 12, 20], [20, 25, 30], 1),  # 20 is not strictly after 20
        ([1, 3, 5], [2, 4, 6], 3),
        ([5, 1, 3], [6, 2, 4], 3),
        ([1, 2, 3], [1, 2, 3], 3),
        ([1, 2], [100, 99], 1),
        ([], [], 0),
    ],
)
def test_max_meetings(start, end, expected):
    assert max_meetings(start, end) == expected
