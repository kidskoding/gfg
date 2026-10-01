import pytest
from helpers import load

search_matrix = load("searching.09_matrix_sorted_search").search_matrix

MAT = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50],
]


@pytest.mark.parametrize(
    "mat, x, expected",
    [
        (MAT, 29, True),
        (MAT, 100, False),
        (MAT, 10, True),  # top-left corner
        (MAT, 50, True),  # bottom-right corner
        (MAT, 9, False),
        (MAT, 31, False),  # within range but absent
        ([[1, 3, 5]], 4, False),
        ([[1], [3], [5]], 5, True),
        ([[1]], 1, True),
        ([], 1, False),
    ],
)
def test_search_matrix(mat, x, expected):
    assert search_matrix(mat, x) is expected
