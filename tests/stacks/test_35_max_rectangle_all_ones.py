import pytest
from helpers import load

max_rectangle = load("stacks.35_max_rectangle_all_ones").max_rectangle


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]], 8),
        ([[0, 1, 1], [1, 1, 1], [0, 1, 1]], 6),
        ([[1, 0, 1], [1, 0, 1], [1, 1, 1]], 3),
        ([[1], [1], [0], [1]], 2),
        ([[1, 1, 1]], 3),
        ([[1]], 1),
        ([[0]], 0),
        ([], 0),
    ],
)
def test_max_rectangle(matrix, expected):
    assert max_rectangle(matrix) == expected
