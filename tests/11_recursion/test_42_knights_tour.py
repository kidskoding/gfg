import pytest
from helpers import load

knights_tour = load("11_recursion.42_knights_tour").knights_tour


def _is_tour(board, n):
    if len(board) != n or any(len(row) != n for row in board):
        return False
    pos = {}
    for r in range(n):
        for c in range(n):
            pos[board[r][c]] = (r, c)
    if sorted(pos) != list(range(n * n)) or pos[0] != (0, 0):
        return False
    for k in range(1, n * n):
        (r1, c1), (r2, c2) = pos[k - 1], pos[k]
        if sorted((abs(r1 - r2), abs(c1 - c2))) != [1, 2]:
            return False
    return True


@pytest.mark.parametrize("n", [2, 3, 4])
def test_knights_tour_impossible(n):
    assert knights_tour(n) is None


def test_knights_tour_single_square():
    assert knights_tour(1) == [[0]]


@pytest.mark.parametrize("n", [5, 6])
def test_knights_tour_valid(n):
    board = knights_tour(n)
    assert board is not None
    assert _is_tour(board, n)
