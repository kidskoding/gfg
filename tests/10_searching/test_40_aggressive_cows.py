import pytest
from helpers import load

aggressive_cows = load("10_searching.40_aggressive_cows").aggressive_cows


@pytest.mark.parametrize(
    "stalls, k, expected",
    [
        ([1, 2, 4, 8, 9], 3, 3),
        ([10, 1, 2, 7, 5], 3, 4),  # unsorted input
        ([2, 12, 11, 3, 26, 7], 5, 1),
        ([1, 2, 3, 4, 5], 3, 2),
        ([5, 1, 9], 2, 8),
        ([0, 100], 2, 100),
        ([1, 2], 2, 1),
    ],
)
def test_aggressive_cows(stalls, k, expected):
    assert aggressive_cows(stalls, k) == expected
