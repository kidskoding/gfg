import pytest
from helpers import load

last_moment = load("01_arrays.29_ants_fall_off_plank").last_moment


@pytest.mark.parametrize(
    "n, left, right, expected",
    [
        (4, [4, 3], [0, 1], 4),
        (7, [], [0, 1, 2, 3, 4, 5, 6, 7], 7),
        (7, [0, 1, 2, 3, 4, 5, 6, 7], [], 7),
        (10, [2], [8], 2),
        (10, [8], [2], 8),
        (5, [], [], 0),
        (9, [5, 1], [3, 6], 6),
    ],
)
def test_last_moment(n, left, right, expected):
    assert last_moment(n, left, right) == expected
