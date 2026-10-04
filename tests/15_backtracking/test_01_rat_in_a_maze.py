import pytest
from helpers import load

rat_in_maze = load("15_backtracking.01_rat_in_a_maze").rat_in_maze


@pytest.mark.parametrize(
    "maze, expected",
    [
        (
            [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]],
            ["DDRDRR", "DRDDRR"],
        ),
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], ["DDRR", "RRDD"]),
        ([[1, 1], [1, 1]], ["DR", "RD"]),
        ([[1, 1, 0], [0, 1, 1], [0, 0, 1]], ["RDRD"]),
        (
            [[1, 1, 1], [1, 1, 1], [0, 0, 1]],
            ["DRRD", "DRURDD", "RDRD", "RRDD"],
        ),  # detours allowed, revisits not
        ([[1, 0], [1, 0]], []),  # destination blocked
        ([[0, 1], [1, 1]], []),  # source blocked
        ([[1]], [""]),
    ],
)
def test_rat_in_maze(maze, expected):
    assert rat_in_maze(maze) == expected
