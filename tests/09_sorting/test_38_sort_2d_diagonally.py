import pytest
from helpers import load

sort_diagonals = load("09_sorting.38_sort_2d_diagonally").sort_diagonals


@pytest.mark.parametrize(
    "mat, expected",
    [
        (
            [[3, 6, 3, 8, 2], [4, 1, 9, 5, 9], [5, 7, 2, 4, 8], [8, 3, 1, 7, 6]],
            [[3, 9, 8, 9, 2], [1, 1, 6, 5, 8], [3, 4, 2, 6, 3], [8, 5, 7, 7, 4]],
        ),
        ([[10, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 6, 3], [4, 5, 2], [7, 8, 9]]),
        ([[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[0, 5, 2], [3, 4, 1], [6, 7, 8]]),
        ([[1, 2, 3], [4, 5, 6]], [[1, 6, 3], [4, 5, 2]]),
        ([[5, 1], [9, 2], [3, 7]], [[5, 1], [7, 2], [3, 9]]),
        (
            [[9, 8, 7, 6], [5, 4, 3, 2], [1, 0, -1, -2]],
            [[9, 8, 7, 6], [0, 4, 3, 2], [1, 5, -1, -2]],
        ),
        ([[1]], [[1]]),
    ],
)
def test_sort_diagonals(mat, expected):
    assert sort_diagonals(mat) is None
    assert mat == expected
