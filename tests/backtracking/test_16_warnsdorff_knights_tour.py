import pytest
from helpers import load

knights_tour = load("backtracking.16_warnsdorff_knights_tour").knights_tour


def _assert_tour(board, n, start):
    assert len(board) == n and all(len(row) == n for row in board)
    where = {board[r][c]: (r, c) for r in range(n) for c in range(n)}
    assert sorted(where) == list(range(1, n * n + 1))
    assert where[1] == tuple(start)
    for step in range(1, n * n):
        (r1, c1), (r2, c2) = where[step], where[step + 1]
        assert sorted([abs(r1 - r2), abs(c1 - c2)]) == [1, 2]


@pytest.mark.parametrize(
    "n, start",
    [
        (1, (0, 0)),
        (5, (0, 0)),
        (5, (2, 2)),
        (6, (0, 0)),
        (7, (3, 3)),
        (8, (0, 0)),
        (8, (3, 4)),
    ],
)
def test_knights_tour(n, start):
    board = knights_tour(n, start)
    assert board is not None
    _assert_tour(board, n, start)


def test_knights_tour_default_start():
    board = knights_tour(6)
    assert board is not None
    _assert_tour(board, 6, (0, 0))


@pytest.mark.parametrize("n", [2, 3, 4])
def test_knights_tour_impossible(n):
    assert knights_tour(n) is None
