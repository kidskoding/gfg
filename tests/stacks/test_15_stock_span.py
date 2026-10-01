import pytest
from helpers import load

stock_span = load("stacks.15_stock_span").stock_span


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([100, 80, 60, 70, 60, 75, 85], [1, 1, 1, 2, 1, 4, 6]),
        ([10, 4, 5, 90, 120, 80], [1, 1, 2, 4, 5, 1]),
        ([3, 3, 3], [1, 2, 3]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 3, 2, 1], [1, 1, 1, 1]),
        ([5], [1]),
        ([], []),
    ],
)
def test_stock_span(prices, expected):
    assert stock_span(prices) == expected
