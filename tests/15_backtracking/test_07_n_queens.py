import pytest
from helpers import load

n_queens = load("15_backtracking.07_n_queens").n_queens


def _is_valid(n, cols):
    rows = range(n)
    return (
        sorted(cols) == list(range(1, n + 1))
        and len({r + c for r, c in zip(rows, cols)}) == n
        and len({r - c for r, c in zip(rows, cols)}) == n
    )


@pytest.mark.parametrize(
    "n, expected",
    [
        (4, [[2, 4, 1, 3], [3, 1, 4, 2]]),
        (1, [[1]]),
        (2, []),
        (3, []),
        (
            5,
            [
                [1, 3, 5, 2, 4],
                [1, 4, 2, 5, 3],
                [2, 4, 1, 3, 5],
                [2, 5, 3, 1, 4],
                [3, 1, 4, 2, 5],
                [3, 5, 2, 4, 1],
                [4, 1, 3, 5, 2],
                [4, 2, 5, 3, 1],
                [5, 2, 4, 1, 3],
                [5, 3, 1, 4, 2],
            ],
        ),
        (
            6,
            [
                [2, 4, 6, 1, 3, 5],
                [3, 6, 2, 5, 1, 4],
                [4, 1, 5, 2, 6, 3],
                [5, 3, 1, 6, 4, 2],
            ],
        ),
    ],
)
def test_n_queens(n, expected):
    assert n_queens(n) == expected


@pytest.mark.parametrize("n, count", [(7, 40), (8, 92)])
def test_n_queens_count(n, count):
    out = n_queens(n)
    assert len(out) == count
    assert out == sorted(out)
    assert len({tuple(s) for s in out}) == count
    assert all(_is_valid(n, s) for s in out)
