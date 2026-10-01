import pytest
from helpers import load

earliest_meeting = load("arrays.32_meeting_scheduler").earliest_meeting


@pytest.mark.parametrize(
    "slots1, slots2, duration, expected",
    [
        ([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8, [60, 68]),
        ([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12, []),
        ([[60, 120], [10, 50], [140, 210]], [[60, 70], [0, 15]], 5, [10, 15]),
        ([[1, 10]], [[2, 3], [5, 9]], 4, [5, 9]),
        ([[0, 5]], [[5, 10]], 0, [5, 5]),
        ([[0, 5]], [[6, 10]], 1, []),
        ([[0, 100]], [[50, 150]], 50, [50, 100]),
    ],
)
def test_earliest_meeting(slots1, slots2, duration, expected):
    assert earliest_meeting(slots1, slots2, duration) == expected
