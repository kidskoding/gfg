import pytest
from helpers import load

celebrity = load("04_two_pointers.22_celebrity_problem").celebrity


@pytest.mark.parametrize(
    "mat, expected",
    [
        ([[0, 1, 0], [0, 0, 0], [0, 1, 0]], 1),
        ([[1, 1, 0], [0, 1, 0], [0, 1, 1]], 1),  # diagonal of 1s is ignored
        ([[0, 1, 1], [0, 0, 1], [0, 0, 0]], 2),
        ([[0, 1, 0], [0, 0, 0], [0, 0, 0]], -1),  # 2 does not know 1
        ([[1, 0], [1, 1]], 0),
        ([[0, 1], [1, 0]], -1),
        ([[0, 0], [0, 0]], -1),
        ([[0]], 0),
    ],
)
def test_celebrity(mat, expected):
    assert celebrity(mat) == expected
