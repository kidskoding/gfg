import pytest
from helpers import load

min_platforms = load("sorting.16_minimum_platforms").min_platforms


@pytest.mark.parametrize(
    "arr, dep, expected",
    [
        ([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000], 3),
        ([900, 1100, 1235], [1000, 1200, 1240], 1),
        ([1000, 1100], [1100, 1200], 2),  # arrival at another's departure time clashes
        ([100, 200, 300, 150], [160, 250, 350, 400], 2),
        ([1, 2, 3], [10, 10, 10], 3),
        ([900], [900], 1),
        ([], [], 0),
    ],
)
def test_min_platforms(arr, dep, expected):
    assert min_platforms(arr, dep) == expected
