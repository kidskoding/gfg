import pytest
from helpers import load

matrix_median = load("10_searching.39_matrix_median").matrix_median


@pytest.mark.parametrize(
    "mat, expected",
    [
        ([[1, 3, 5], [2, 6, 9], [3, 6, 9]], 5),
        ([[2, 4, 9], [3, 6, 7], [4, 7, 10]], 6),
        ([[1, 10, 20], [2, 3, 30], [4, 5, 6]], 5),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 2]], 1),
        ([[3], [1], [2]], 2),  # single column
        ([[1, 3, 4]], 3),  # single row
        ([[7]], 7),
    ],
)
def test_matrix_median(mat, expected):
    assert matrix_median(mat) == expected
