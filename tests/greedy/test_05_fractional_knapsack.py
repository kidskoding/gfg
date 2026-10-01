import pytest
from helpers import load

fractional_knapsack = load("greedy.05_fractional_knapsack").fractional_knapsack


@pytest.mark.parametrize(
    "values, weights, capacity, expected",
    [
        ([60, 100, 120], [10, 20, 30], 50, 240.0),
        ([60, 100], [10, 20], 50, 160.0),  # everything fits
        ([10, 20, 30], [5, 10, 15], 100, 60.0),
        ([5, 8], [2, 4], 5, 11.0),  # 5 + 3/4 of 8
        ([500], [30], 10, 500 * 10 / 30),
        ([60, 100, 120], [10, 20, 30], 0, 0.0),
        ([], [], 10, 0.0),
    ],
)
def test_fractional_knapsack(values, weights, capacity, expected):
    assert fractional_knapsack(values, weights, capacity) == pytest.approx(expected)
