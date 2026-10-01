import pytest
from helpers import load

min_platforms = load("greedy.06_minimum_platforms").min_platforms


@pytest.mark.parametrize(
    "arr, dep, expected",
    [
        ([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000], 3),
        ([900, 1235, 1100], [1000, 1240, 1200], 1),
        ([1000, 935, 1100], [1200, 1240, 1130], 3),
        ([900, 910], [910, 920], 2),  # arrival at the same minute as a departure
        ([900, 900, 900], [1000, 1000, 1000], 3),
        ([100, 200, 300], [150, 250, 350], 1),
        ([900], [910], 1),
        ([], [], 0),
    ],
)
def test_min_platforms(arr, dep, expected):
    assert min_platforms(arr, dep) == expected
