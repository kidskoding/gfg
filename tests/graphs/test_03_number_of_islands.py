import pytest
from helpers import load

num_islands = load("graphs.03_number_of_islands").num_islands


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [1, 0, 0, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 1, 1, 0],
            ],
            4,
        ),
        ([[1, 0], [0, 1]], 1),  # diagonal neighbours join
        ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 4),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1),
        ([[0, 0], [0, 0]], 0),
        ([[1]], 1),
        ([[0]], 0),
    ],
)
def test_num_islands(grid, expected):
    before = [row[:] for row in grid]
    assert num_islands(grid) == expected
    assert grid == before
