import pytest
from helpers import load

min_knight_steps = load("07_queues.14_knight_min_steps").min_knight_steps


@pytest.mark.parametrize(
    "n, knight, target, expected",
    [
        (6, (3, 4), (0, 0), 3),  # GFG example (1-indexed (4,5) -> (1,1))
        (8, (0, 0), (7, 7), 6),
        (8, (0, 0), (1, 1), 4),  # corner makes the diagonal neighbour far
        (8, (0, 0), (0, 1), 3),
        (8, (3, 3), (4, 5), 1),
        (3, (0, 0), (2, 1), 1),
        (3, (0, 0), (1, 1), -1),  # centre of 3x3 is unreachable
        (2, (0, 0), (1, 1), -1),
        (5, (2, 2), (2, 2), 0),
        (1, (0, 0), (0, 0), 0),
    ],
)
def test_min_knight_steps(n, knight, target, expected):
    assert min_knight_steps(n, knight, target) == expected
