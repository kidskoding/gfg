from itertools import pairwise

import pytest
from helpers import load

path_to_middle = load("backtracking.09_path_to_middle_cell").path_to_middle

GFG_MAZE = [
    [3, 5, 4, 4, 7, 3, 4, 6, 3],
    [6, 7, 5, 6, 6, 2, 6, 6, 2],
    [3, 3, 4, 3, 2, 5, 4, 7, 2],
    [6, 5, 5, 1, 2, 3, 6, 5, 6],
    [3, 3, 4, 3, 0, 1, 4, 3, 4],
    [3, 5, 4, 3, 2, 2, 3, 3, 5],
    [3, 5, 4, 3, 2, 6, 4, 4, 3],
    [3, 5, 1, 3, 7, 5, 3, 6, 4],
    [6, 2, 4, 3, 4, 5, 4, 5, 1],
]


def _assert_valid(maze, path):
    n = len(maze)
    assert tuple(path[0]) in {(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n - 1)}
    assert tuple(path[-1]) == (n // 2, n // 2)
    assert len({tuple(p) for p in path}) == len(path)
    for (r, c), (nr, nc) in pairwise(path):
        jump = maze[r][c]
        assert 0 <= nr < n and 0 <= nc < n
        assert (abs(nr - r), abs(nc - c)) in {(jump, 0), (0, jump)} and jump > 0


@pytest.mark.parametrize(
    "maze",
    [
        GFG_MAZE,
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[3, 3, 3], [3, 0, 1], [3, 3, 1]],  # only the bottom-right corner can move
        [
            [2, 9, 9, 9, 9],
            [9, 9, 9, 9, 9],
            [9, 9, 0, 9, 9],
            [9, 9, 9, 9, 9],
            [2, 9, 2, 9, 9],
        ],
        [[7]],  # 1 x 1: the corner is the middle
    ],
)
def test_path_to_middle_found(maze):
    path = path_to_middle(maze)
    assert path is not None
    _assert_valid(maze, path)


@pytest.mark.parametrize(
    "maze",
    [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],  # nobody can move
        [[3, 1, 3], [1, 0, 1], [3, 1, 3]],  # corner jumps leave the board
        [
            [2, 9, 9, 9, 2],
            [9, 9, 9, 9, 9],
            [9, 9, 0, 9, 9],
            [9, 9, 9, 9, 9],
            [2, 9, 9, 9, 2],
        ],  # corner jumps land on dead ends
    ],
)
def test_path_to_middle_none(maze):
    assert path_to_middle(maze) is None
