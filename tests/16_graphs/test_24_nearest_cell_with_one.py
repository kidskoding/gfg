import pytest
from helpers import load

nearest_one_distance = load("16_graphs.24_nearest_cell_with_one").nearest_one_distance


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1]],
            [[1, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0]],
        ),
        ([[1, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 1, 2], [1, 2, 3], [2, 3, 4]]),
        ([[0, 0, 0, 1]], [[3, 2, 1, 0]]),
        ([[0], [1], [0]], [[1], [0], [1]]),
        ([[1, 0, 0, 0, 1]], [[0, 1, 2, 1, 0]]),
        ([[1, 1], [1, 1]], [[0, 0], [0, 0]]),
        ([[1]], [[0]]),
    ],
)
def test_nearest_one_distance(grid, expected):
    before = [row[:] for row in grid]
    assert nearest_one_distance(grid) == expected
    assert grid == before
