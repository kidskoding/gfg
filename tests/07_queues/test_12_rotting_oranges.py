import copy

import pytest
from helpers import load

rot_time = load("07_queues.12_rotting_oranges").rot_time


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]], 2),
        ([[2, 1, 0, 2, 1], [0, 0, 1, 2, 1], [1, 0, 0, 2, 1]], -1),
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
        ([[2, 1, 1, 1, 1]], 4),
        ([[1, 1, 1, 1, 2]], 4),
        ([[2, 1, 1, 1, 2]], 2),  # two sources meet in the middle
        ([[0, 2]], 0),
        ([[1]], -1),
        ([[0, 0], [0, 0]], 0),
        ([], 0),
    ],
)
def test_rot_time(grid, expected):
    original = copy.deepcopy(grid)
    assert rot_time(grid) == expected
    assert grid == original
