import pytest
from helpers import load

min_cost_path = load("16_graphs.35_min_cost_path").min_cost_path


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[9, 4, 9, 9], [6, 7, 6, 4], [8, 3, 3, 7], [7, 4, 9, 10]], 43),
        ([[4, 4], [3, 7]], 14),
        ([[1, 100, 1, 1, 1], [1, 100, 1, 100, 1], [1, 1, 1, 100, 1]], 11),  # must go up
        ([[1, 2, 3]], 6),
        ([[1], [2], [3]], 6),
        ([[5]], 5),
    ],
)
def test_min_cost_path(grid, expected):
    assert min_cost_path(grid) == expected
