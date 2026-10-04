import pytest
from helpers import load

longest_path = load("18_dynamic_programming.06_longest_path_in_matrix").longest_path


@pytest.mark.parametrize(
    "mat, expected",
    [
        ([[1, 2, 9], [5, 3, 8], [4, 6, 7]], 4),
        ([[1, 2, 3], [6, 5, 4], [7, 8, 9]], 9),  # snake through every cell
        ([[1, 3], [5, 7]], 1),  # no adjacent +1 step
        ([[5]], 1),
        ([[1, 2, 3, 4]], 4),
        ([[3, 2, 1]], 3),  # path may run right-to-left
        ([[1, 1], [2, 2]], 2),  # duplicates
        ([], 0),
    ],
)
def test_longest_path(mat, expected):
    assert longest_path(mat) == expected
