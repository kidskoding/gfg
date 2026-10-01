import pytest
from helpers import load

shortest_safe_route = load("backtracking.20_shortest_safe_route").shortest_safe_route

GFG_GRID = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
]


@pytest.mark.parametrize(
    "grid, expected",
    [
        (GFG_GRID, 13),
        ([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 3),
        (
            [[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
            3,
        ),  # bottom row stays clear
        ([[1], [1]], 0),  # first column is the last column
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], -1),  # mine's neighbours cut every row
        ([[1, 1, 0, 1, 1], [1, 1, 0, 1, 1]], -1),  # wall of mines
        ([[0]], -1),
    ],
)
def test_shortest_safe_route(grid, expected):
    assert shortest_safe_route(grid) == expected
