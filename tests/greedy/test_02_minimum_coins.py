import pytest
from helpers import load

min_coins = load("greedy.02_minimum_coins").min_coins

DENOMINATIONS = {1, 2, 5, 10, 20, 50, 100, 500, 1000}


@pytest.mark.parametrize(
    "amount, expected_count",
    [
        (70, 2),  # 50 + 20
        (121, 3),  # 100 + 20 + 1
        (93, 5),  # 50 + 20 + 20 + 2 + 1
        (2888, 12),
        (4, 2),  # 2 + 2
        (8, 3),  # 5 + 2 + 1
        (1, 1),
        (0, 0),
    ],
)
def test_min_coins(amount, expected_count):
    coins = min_coins(amount)
    assert sum(coins) == amount
    assert all(c in DENOMINATIONS for c in coins)
    assert coins == sorted(coins, reverse=True)
    assert len(coins) == expected_count
