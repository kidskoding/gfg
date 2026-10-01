import pytest
from helpers import load

articulation_points = load("graphs.37_articulation_points").articulation_points


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (5, [(0, 1), (1, 4), (2, 3), (2, 4), (3, 4)], [1, 4]),
        (4, [(0, 1), (1, 2), (2, 3)], [1, 2]),
        (4, [(0, 1), (0, 2), (0, 3)], [0]),
        (5, [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 2)], [2]),  # bow-tie
        (5, [(0, 1), (1, 2), (3, 4)], [1]),  # disconnected
        (3, [(0, 1), (1, 2), (2, 0)], []),
        (2, [(0, 1)], []),
        (1, [], []),
    ],
)
def test_articulation_points(n, edges, expected):
    assert articulation_points(n, edges) == expected
