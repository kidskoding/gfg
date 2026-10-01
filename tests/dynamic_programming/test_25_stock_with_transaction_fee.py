import pytest
from helpers import load

max_profit_with_fee = load(
    "dynamic_programming.25_stock_with_transaction_fee"
).max_profit_with_fee


@pytest.mark.parametrize(
    "prices, fee, expected",
    [
        ([1, 3, 2, 8, 4, 9], 2, 8),
        ([1, 3, 7, 5, 10, 3], 3, 6),
        ([6, 1, 7, 2, 8, 4], 2, 8),
        ([9, 7, 5, 3], 1, 0),
        ([1, 5], 5, 0),
        ([1, 5], 0, 4),
        ([5], 1, 0),
        ([], 1, 0),
    ],
)
def test_max_profit_with_fee(prices, fee, expected):
    assert max_profit_with_fee(prices, fee) == expected
