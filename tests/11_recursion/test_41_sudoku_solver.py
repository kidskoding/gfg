import copy

import pytest
from helpers import load

solve_sudoku = load("11_recursion.41_sudoku_solver").solve_sudoku

GFG_PUZZLE = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

GFG_SOLUTION = [
    [3, 1, 6, 5, 7, 8, 4, 9, 2],
    [5, 2, 9, 1, 3, 4, 7, 6, 8],
    [4, 8, 7, 6, 2, 9, 5, 3, 1],
    [2, 6, 3, 4, 1, 5, 9, 8, 7],
    [9, 7, 4, 8, 6, 3, 1, 2, 5],
    [8, 5, 1, 7, 9, 2, 6, 4, 3],
    [1, 3, 8, 9, 4, 7, 2, 5, 6],
    [6, 9, 2, 3, 5, 1, 8, 7, 4],
    [7, 4, 5, 2, 8, 6, 3, 1, 9],
]

LEETCODE_PUZZLE = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def _one_blank():
    board = copy.deepcopy(GFG_SOLUTION)
    board[4][4] = 0
    return board


def _is_solved(board):
    digits = set(range(1, 10))
    rows = [set(r) for r in board]
    cols = [{board[r][c] for r in range(9)} for c in range(9)]
    boxes = [
        {board[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)}
        for br in (0, 3, 6)
        for bc in (0, 3, 6)
    ]
    return all(group == digits for group in rows + cols + boxes)


@pytest.mark.parametrize(
    "puzzle",
    [
        GFG_PUZZLE,
        LEETCODE_PUZZLE,
        GFG_SOLUTION,
        _one_blank(),
        [[0] * 9 for _ in range(9)],
    ],
    ids=["gfg", "leetcode", "already_solved", "one_blank", "empty"],
)
def test_solve_sudoku_valid(puzzle):
    board = copy.deepcopy(puzzle)
    assert solve_sudoku(board) is True
    assert _is_solved(board)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]:
                assert board[r][c] == puzzle[r][c]  # givens untouched


def test_solve_sudoku_gfg_exact():
    board = copy.deepcopy(GFG_PUZZLE)
    solve_sudoku(board)
    assert board == GFG_SOLUTION  # puzzle has a unique solution


def test_solve_sudoku_unsolvable():
    board = [[0] * 9 for _ in range(9)]
    board[0] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    board[1][0] = 9  # (0, 0) needs a 9 but column 0 already has one
    assert solve_sudoku(board) is False
