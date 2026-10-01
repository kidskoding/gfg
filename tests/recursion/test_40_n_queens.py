import pytest
from helpers import load

n_queens = load("recursion.40_n_queens").n_queens


def _valid(sol, n):
    if sorted(sol) != list(range(1, n + 1)):
        return False
    return all(abs(sol[i] - sol[j]) != j - i for i in range(n) for j in range(i + 1, n))


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, [[1]]),
        (2, []),
        (3, []),
        (4, [[2, 4, 1, 3], [3, 1, 4, 2]]),
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
    assert sorted(n_queens(n)) == sorted(expected)


@pytest.mark.parametrize("n, count", [(5, 10), (7, 40), (8, 92)])
def test_n_queens_counts(n, count):
    result = n_queens(n)
    assert len(result) == count
    assert len({tuple(s) for s in result}) == count
    assert all(_valid(s, n) for s in result)
