import pytest
from helpers import load

maximize_array = load("heaps.18_maximize_the_array").maximize_array


@pytest.mark.parametrize(
    "arr1, arr2, expected",
    [
        ([7, 4, 8, 0, 1], [9, 7, 2, 3, 6], [9, 7, 6, 4, 8]),
        ([6, 7, 5, 3], [5, 6, 2, 9], [5, 6, 9, 7]),
        ([3, 3], [1, 2], [2, 3]),  # duplicates collapse
        ([1, 2, 3], [1, 2, 3], [1, 2, 3]),
        ([10, 20], [1, 2], [10, 20]),  # nothing from arr2 makes the cut
        ([1], [2], [2]),
    ],
)
def test_maximize_array(arr1, arr2, expected):
    assert maximize_array(arr1, arr2) == expected
