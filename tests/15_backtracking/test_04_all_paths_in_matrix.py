import pytest
from helpers import load

all_paths = load("15_backtracking.04_all_paths_in_matrix").all_paths


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[1, 2, 3], [4, 5, 6]], [[1, 4, 5, 6], [1, 2, 5, 6], [1, 2, 3, 6]]),
        ([[1, 2], [3, 4]], [[1, 2, 4], [1, 3, 4]]),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [
                [1, 2, 3, 6, 9],
                [1, 2, 5, 6, 9],
                [1, 2, 5, 8, 9],
                [1, 4, 5, 6, 9],
                [1, 4, 5, 8, 9],
                [1, 4, 7, 8, 9],
            ],
        ),
        ([[1, 1], [1, 1]], [[1, 1, 1], [1, 1, 1]]),  # identical value paths both listed
        ([[1, 2, 3]], [[1, 2, 3]]),
        ([[1], [2], [3]], [[1, 2, 3]]),
        ([[5]], [[5]]),
    ],
)
def test_all_paths(grid, expected):
    assert sorted(all_paths(grid)) == sorted(expected)
