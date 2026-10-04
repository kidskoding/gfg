import pytest
from helpers import load

find_celebrity = load("06_stacks.26_celebrity_problem").find_celebrity


@pytest.mark.parametrize(
    "m, expected",
    [
        ([[0, 1, 0], [0, 0, 0], [0, 1, 0]], 1),
        ([[0, 1], [1, 0]], -1),
        ([[1, 1, 0], [0, 1, 0], [0, 1, 1]], 1),
        ([[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]], 2),
        ([[0, 1, 1], [0, 0, 0], [0, 1, 0]], 1),
        ([[0, 0], [0, 0]], -1),
        ([[0]], 0),
        ([], -1),
    ],
)
def test_find_celebrity(m, expected):
    assert find_celebrity(m) == expected
