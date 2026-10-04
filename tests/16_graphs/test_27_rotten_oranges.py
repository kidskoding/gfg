import pytest
from helpers import load

oranges_rotting = load("16_graphs.27_rotten_oranges").oranges_rotting


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[0, 1, 2], [0, 1, 2], [2, 1, 1]], 1),
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1, 1, 1]], 4),
        ([[2, 1, 0, 1]], -1),  # last orange is cut off
        ([[1, 1], [1, 1]], -1),  # nothing rotten
        ([[0, 2]], 0),  # no fresh oranges
        ([[0]], 0),
        ([[1]], -1),
    ],
)
def test_oranges_rotting(grid, expected):
    assert oranges_rotting(grid) == expected
