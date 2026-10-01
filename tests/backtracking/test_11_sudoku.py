import copy

import pytest
from helpers import load

solve_sudoku = load("backtracking.11_sudoku").solve_sudoku

GFG_BOARD = [
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
GFG_SOLVED = [
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
LEETCODE_BOARD = [
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


def _assert_solved(board, givens):
    digits = list(range(1, 10))
    for i in range(9):
        assert sorted(board[i]) == digits
        assert sorted(row[i] for row in board) == digits
        br, bc = 3 * (i // 3), 3 * (i % 3)
        assert (
            sorted(board[br + r][bc + c] for r in range(3) for c in range(3)) == digits
        )
    for r in range(9):
        for c in range(9):
            if givens[r][c]:
                assert board[r][c] == givens[r][c]


@pytest.mark.parametrize(
    "givens",
    [
        GFG_BOARD,
        LEETCODE_BOARD,
        GFG_SOLVED,  # already complete
        [[0] * 9 for _ in range(9)],  # empty board: any valid grid
    ],
)
def test_solve_sudoku(givens):
    board = copy.deepcopy(givens)
    assert solve_sudoku(board) is True
    _assert_solved(board, givens)


def test_solve_sudoku_gfg_exact():
    board = copy.deepcopy(GFG_BOARD)
    solve_sudoku(board)
    assert board == GFG_SOLVED


def test_solve_sudoku_unsolvable():
    board = [[0] * 9 for _ in range(9)]
    board[0][:8] = [1, 2, 3, 4, 5, 6, 7, 8]
    board[4][8] = 9  # (0, 8) needs 9 but column 8 already has one
    assert solve_sudoku(board) is False
