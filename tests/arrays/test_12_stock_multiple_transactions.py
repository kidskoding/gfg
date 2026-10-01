import pytest
from helpers import load

max_profit_multi = load("arrays.12_stock_multiple_transactions").max_profit_multi


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([100, 180, 260, 310, 40, 535, 695], 865),
        ([4, 2, 2, 2, 4], 2),
        ([7, 1, 5, 3, 6, 4], 7),
        ([5, 4, 3, 2, 1], 0),
        ([1, 2, 3, 4, 5], 4),
        ([3], 0),
        ([], 0),
    ],
)
def test_max_profit_multi(prices, expected):
    assert max_profit_multi(prices) == expected
