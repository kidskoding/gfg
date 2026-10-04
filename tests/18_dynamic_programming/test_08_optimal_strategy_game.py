import pytest
from helpers import load

optimal_strategy = load("18_dynamic_programming.08_optimal_strategy_game").optimal_strategy


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([5, 3, 7, 10], 15),
        ([8, 15, 3, 7], 22),
        ([2, 2, 2, 2], 4),
        ([20, 30, 2, 2, 2, 10], 42),
        ([1, 100, 1, 1], 101),
        ([4, 9], 9),
        ([7], 7),
        ([], 0),
    ],
)
def test_optimal_strategy(arr, expected):
    assert optimal_strategy(arr) == expected
