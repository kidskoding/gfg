import pytest
from helpers import load

trap_rain_water = load("04_two_pointers.23_trapping_rain_water").trap_rain_water


@pytest.mark.parametrize(
    "heights, expected",
    [
        ([3, 0, 1, 0, 4, 0, 2], 10),
        ([3, 0, 2, 0, 4], 7),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([2, 0, 2], 2),
        ([1, 2, 3, 4], 0),
        ([5], 0),
        ([], 0),
    ],
)
def test_trap_rain_water(heights, expected):
    assert trap_rain_water(heights) == expected
