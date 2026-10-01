import pytest
from helpers import load

shortest_path_k_walls = load("graphs.42_shortest_path_k_walls").shortest_path_k_walls


@pytest.mark.parametrize(
    "grid, k, expected",
    [
        ([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1, 6),
        ([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1, -1),
        ([[0, 0, 0], [0, 0, 1], [0, 1, 0]], 1, 4),
        ([[0, 0, 0], [0, 0, 1], [0, 1, 0]], 0, -1),
        ([[0, 1], [1, 0]], 1, 2),
        ([[0, 1], [1, 0]], 0, -1),
        ([[0, 0, 0]], 0, 2),
        ([[0]], 0, 0),
    ],
)
def test_shortest_path_k_walls(grid, k, expected):
    assert shortest_path_k_walls(grid, k) == expected
