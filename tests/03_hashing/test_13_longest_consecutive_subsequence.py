import pytest
from helpers import load

longest_consecutive = load(
    "03_hashing.13_longest_consecutive_subsequence"
).longest_consecutive


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 6, 1, 9, 4, 5, 3], 6),
        ([1, 9, 3, 10, 4, 20, 2], 4),
        ([15, 13, 12, 14, 11, 10, 9], 7),
        ([1, 2, 2, 3], 3),  # duplicates count once
        ([10, 30, 20], 1),
        ([-1, 0, 1, -2], 4),
        ([7], 1),
        ([], 0),
    ],
)
def test_longest_consecutive(arr, expected):
    assert longest_consecutive(arr) == expected
