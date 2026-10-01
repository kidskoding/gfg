import pytest
from helpers import load

trap_water = load("arrays.38_trapping_rain_water").trap_water


@pytest.mark.parametrize(
    "heights, expected",
    [
        ([3, 0, 1, 0, 4, 0, 2], 10),
        ([3, 0, 2, 0, 4], 7),
        ([1, 2, 3, 4], 0),
        ([10, 9, 0, 5], 5),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([5], 0),
        ([], 0),
        ([2, 2, 2], 0),
    ],
)
def test_trap_water(heights, expected):
    assert trap_water(heights) == expected
