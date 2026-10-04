import pytest
from helpers import load

ship_within_days = load("10_searching.27_ship_within_days").ship_within_days


@pytest.mark.parametrize(
    "weights, d, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15),
        ([3, 2, 2, 4, 1, 4], 3, 6),
        ([1, 2, 3, 1, 1], 4, 3),
        ([10, 50, 100, 100, 50, 100, 100, 100], 5, 160),
        ([1, 2, 3, 4, 5], 1, 15),  # one day: total weight
        ([1, 2, 3, 4, 5], 5, 5),  # one per day: heaviest package
        ([9], 3, 9),
    ],
)
def test_ship_within_days(weights, d, expected):
    assert ship_within_days(weights, d) == expected
