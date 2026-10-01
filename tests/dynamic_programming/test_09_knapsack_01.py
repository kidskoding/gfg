import pytest
from helpers import load

knapsack = load("dynamic_programming.09_knapsack_01").knapsack


@pytest.mark.parametrize(
    "capacity, values, weights, expected",
    [
        (4, [1, 2, 3], [4, 5, 1], 3),
        (3, [1, 2, 3], [4, 5, 6], 0),
        (5, [10, 40, 30, 50], [5, 4, 6, 3], 50),
        (10, [10, 40, 30, 50], [5, 4, 6, 3], 90),
        (50, [60, 100, 120], [10, 20, 30], 220),
        (0, [5], [1], 0),
        (10, [], [], 0),
        (6, [5, 5, 5], [2, 2, 2], 15),  # duplicates
    ],
)
def test_knapsack(capacity, values, weights, expected):
    assert knapsack(capacity, values, weights) == expected
