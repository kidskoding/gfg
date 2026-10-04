import pytest
from helpers import load

min_time_orders = load("10_searching.44_min_time_all_orders").min_time_orders


@pytest.mark.parametrize(
    "ranks, n, expected",
    [
        ([1, 2, 3, 4], 10, 12),
        ([1, 1, 1, 1, 1, 1, 1, 1], 8, 1),  # one item each
        ([1], 8, 36),
        ([2, 1], 3, 3),
        ([5, 5], 4, 15),
        ([1, 2], 1, 1),
        ([3], 1, 3),
    ],
)
def test_min_time_orders(ranks, n, expected):
    assert min_time_orders(ranks, n) == expected
