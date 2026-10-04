import pytest
from helpers import load

closed_islands = load("16_graphs.41_closed_islands").closed_islands


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 1, 1, 1, 0, 0, 1],
                [0, 1, 0, 1, 0, 0, 0, 1],
                [0, 1, 1, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1],
            ],
            2,
        ),
        (
            [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]],
            2,
        ),  # diagonal not joined
        ([[0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]], 0),  # reaches the border
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 1),
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 0),
        ([[0, 0], [0, 0]], 0),
        ([[1]], 0),
    ],
)
def test_closed_islands(grid, expected):
    assert closed_islands(grid) == expected
