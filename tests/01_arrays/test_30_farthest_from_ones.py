import pytest
from helpers import load

max_dist_to_closest = load("01_arrays.30_farthest_from_ones").max_dist_to_closest


@pytest.mark.parametrize(
    "seats, expected",
    [
        ([1, 0, 0, 0, 1, 0, 1], 2),
        ([1, 0, 0, 0], 3),
        ([0, 1], 1),
        ([0, 0, 0, 1, 0], 3),
        ([1, 0, 1], 1),
        ([1, 0, 0, 0, 0, 1], 2),
        ([1, 0, 0, 0, 0, 0, 1], 3),
    ],
)
def test_max_dist_to_closest(seats, expected):
    assert max_dist_to_closest(seats) == expected
