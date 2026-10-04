import pytest
from helpers import load

longest_mountain = load("01_arrays.33_longest_mountain").longest_mountain


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 1, 4, 7, 3, 2, 5], 5),
        ([2, 2, 2], 0),
        ([1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5], 11),
        ([1, 2, 3], 0),
        ([3, 2, 1], 0),
        ([1, 2, 2, 1], 0),
        ([0, 1, 0], 3),
        ([], 0),
    ],
)
def test_longest_mountain(arr, expected):
    assert longest_mountain(arr) == expected
