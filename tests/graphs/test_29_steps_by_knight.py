import pytest
from helpers import load

min_knight_steps = load("graphs.29_steps_by_knight").min_knight_steps


@pytest.mark.parametrize(
    "n, knight, target, expected",
    [
        (6, (3, 4), (0, 0), 3),
        (8, (0, 0), (7, 7), 6),
        (8, (0, 0), (1, 2), 1),
        (8, (0, 0), (1, 1), 4),  # corner to its diagonal neighbour
        (8, (4, 4), (4, 4), 0),
        (3, (0, 0), (1, 1), -1),  # centre of 3x3 is unreachable
        (2, (0, 0), (1, 1), -1),
        (1, (0, 0), (0, 0), 0),
    ],
)
def test_min_knight_steps(n, knight, target, expected):
    assert min_knight_steps(n, knight, target) == expected
