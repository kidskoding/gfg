import pytest
from helpers import load

can_pair_divisible = load("03_hashing.14_pair_sum_divisible_by_k").can_pair_divisible


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([9, 5, 7, 3], 6, True),
        ([91, 74, 66, 48], 10, False),
        ([92, 75, 65, 48, 45, 35], 10, True),
        ([1, 2, 3], 3, False),  # odd length
        ([3, 3, 3], 3, False),
        ([6, 12], 6, True),  # remainder 0 pairs with remainder 0
        ([2, 2, 2, 2], 4, True),  # remainder k/2 pairs with itself
        ([2, 2, 2, 6], 4, True),
        ([1, 1, 2, 2], 3, True),
        ([], 5, True),
    ],
)
def test_can_pair_divisible(arr, k, expected):
    assert can_pair_divisible(arr, k) is expected
