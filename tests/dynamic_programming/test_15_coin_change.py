import pytest
from helpers import load

coin_change_ways = load("dynamic_programming.15_coin_change").coin_change_ways


@pytest.mark.parametrize(
    "coins, total, expected",
    [
        ([1, 2, 3], 4, 4),
        ([2, 5, 3, 6], 10, 5),
        ([10], 10, 1),
        ([5, 10], 3, 0),
        ([1, 2], 0, 1),
        ([1], 7, 1),
        ([], 0, 1),
        ([], 5, 0),
    ],
)
def test_coin_change_ways(coins, total, expected):
    assert coin_change_ways(coins, total) == expected
