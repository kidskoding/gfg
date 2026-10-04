import pytest
from helpers import load

all_paths = load("11_recursion.29_all_matrix_paths").all_paths


def _norm(paths):
    return sorted(tuple(p) for p in paths)


@pytest.mark.parametrize(
    "mat, expected",
    [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [
                [1, 4, 7, 8, 9],
                [1, 4, 5, 8, 9],
                [1, 4, 5, 6, 9],
                [1, 2, 5, 8, 9],
                [1, 2, 5, 6, 9],
                [1, 2, 3, 6, 9],
            ],
        ),
        ([[1, 2, 3], [4, 5, 6]], [[1, 4, 5, 6], [1, 2, 5, 6], [1, 2, 3, 6]]),
        ([[1, 2], [3, 4]], [[1, 3, 4], [1, 2, 4]]),
        ([[1, 2, 3]], [[1, 2, 3]]),
        ([[1], [2], [3]], [[1, 2, 3]]),
        ([[7]], [[7]]),
        (
            [[0, 0], [0, 0]],
            [[0, 0, 0], [0, 0, 0]],
        ),  # equal values: both paths still listed
    ],
)
def test_all_paths(mat, expected):
    assert _norm(all_paths(mat)) == _norm(expected)


def test_all_paths_count():
    mat = [[r * 4 + c for c in range(4)] for r in range(4)]
    paths = all_paths(mat)
    assert len(paths) == 20
    assert len(set(map(tuple, paths))) == 20
    assert all(len(p) == 7 and p[0] == 0 and p[-1] == 15 for p in paths)
