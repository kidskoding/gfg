import pytest
from helpers import load

most_booked_room = load("14_heaps.21_room_with_max_meetings").most_booked_room


@pytest.mark.parametrize(
    "n, meetings, expected",
    [
        (2, [(0, 10), (1, 5), (2, 7), (3, 4)], 0),
        (3, [(1, 20), (2, 10), (3, 5), (4, 9), (6, 8)], 1),
        (2, [(0, 5), (1, 2), (2, 3), (3, 4)], 1),  # room 1 frees up first every time
        (
            2,
            [(0, 10), (1, 9), (2, 3)],
            1,
        ),  # delayed meeting takes the earliest-freed room
        (2, [(0, 10), (1, 10), (2, 3), (4, 5)], 0),  # both free at 10: lowest room wins
        (3, [(5, 6), (1, 2), (3, 4)], 0),  # unsorted input, room 0 always free
        (1, [(0, 1), (1, 2)], 0),
        (3, [(0, 1)], 0),
    ],
)
def test_most_booked_room(n, meetings, expected):
    assert most_booked_room(n, meetings) == expected
