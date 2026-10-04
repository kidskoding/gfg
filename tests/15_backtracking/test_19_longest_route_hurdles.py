import pytest
from helpers import load

longest_route = load("15_backtracking.19_longest_route_hurdles").longest_route

GFG_GRID = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
OPEN_3X3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]


@pytest.mark.parametrize(
    "grid, src, dst, expected",
    [
        (GFG_GRID, (0, 0), (1, 7), 24),
        ([[1, 1], [1, 1]], (0, 0), (0, 1), 3),  # go the long way round
        (OPEN_3X3, (0, 0), (2, 2), 8),  # snake through every cell
        (OPEN_3X3, (0, 0), (0, 1), 7),  # parity leaves one cell unvisited
        (OPEN_3X3, (1, 1), (1, 1), 0),
        ([[1, 0, 1]], (0, 0), (0, 2), -1),
        ([[0, 1], [1, 1]], (0, 0), (1, 1), -1),  # src is a hurdle
        ([[1, 1], [1, 0]], (0, 0), (1, 1), -1),  # dst is a hurdle
    ],
)
def test_longest_route(grid, src, dst, expected):
    assert longest_route(grid, src, dst) == expected
