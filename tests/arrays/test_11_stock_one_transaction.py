import pytest
from helpers import load

max_profit_one = load("arrays.11_stock_one_transaction").max_profit_one


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 10, 1, 3, 6, 9, 2], 8),
        ([7, 6, 4, 3, 1], 0),
        ([1, 3, 6, 9, 11], 10),
        ([5], 0),
        ([], 0),
        ([2, 4, 1], 2),
        ([3, 3, 3], 0),
    ],
)
def test_max_profit_one(prices, expected):
    assert max_profit_one(prices) == expected
