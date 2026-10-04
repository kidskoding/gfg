import pytest
from helpers import load

leaders = load("01_arrays.15_array_leaders").leaders


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([16, 17, 4, 3, 5, 2], [17, 5, 2]),
        ([10, 4, 2, 4, 1], [10, 4, 4, 1]),
        ([5, 10, 20, 40], [40]),
        ([30, 10, 10, 5], [30, 10, 10, 5]),
        ([7], [7]),
        ([], []),
        ([-1, -5, -3], [-1, -3]),
    ],
)
def test_leaders(arr, expected):
    assert leaders(arr) == expected
