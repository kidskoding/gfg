import pytest
from helpers import load

lis_length = load("dynamic_programming.02_longest_increasing_subsequence").lis_length


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([3, 10, 2, 1, 20], 3),
        ([30, 20, 10], 1),
        ([10, 20, 35, 80], 4),
        ([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 6),
        ([2, 2, 2], 1),  # strictly increasing
        ([-1, -2, 0, 3], 3),
        ([7], 1),
        ([], 0),
    ],
)
def test_lis_length(arr, expected):
    assert lis_length(arr) == expected
