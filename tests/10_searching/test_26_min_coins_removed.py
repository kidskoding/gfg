import pytest
from helpers import load

min_coins_removed = load("10_searching.26_min_coins_removed").min_coins_removed


@pytest.mark.parametrize(
    "piles, k, expected",
    [
        ([2, 2, 2, 2], 0, 0),
        ([1, 5, 1, 2, 5, 1], 3, 2),
        ([1, 2, 3], 0, 2),
        ([1, 100], 10, 1),  # cheaper to empty the small pile
        ([4, 7, 10], 3, 3),
        ([3, 3, 9], 2, 4),
        ([5], 0, 0),
    ],
)
def test_min_coins_removed(piles, k, expected):
    assert min_coins_removed(piles, k) == expected
