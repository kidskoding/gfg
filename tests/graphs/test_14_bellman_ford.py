import pytest
from helpers import load

bellman_ford = load("graphs.14_bellman_ford").bellman_ford


@pytest.mark.parametrize(
    "n, edges, src, expected",
    [
        (
            5,
            [(1, 3, 2), (4, 3, -1), (2, 4, 1), (1, 2, 1), (0, 1, 5)],
            0,
            [0, 5, 6, 6, 7],
        ),
        (3, [(0, 1, 4), (0, 2, 5), (2, 1, -3)], 0, [0, 2, 5]),
        (3, [(0, 1, -2)], 0, [0, -2, None]),
        (3, [(0, 1, 1), (1, 2, 1)], 1, [None, 0, 1]),  # edges are directed
        (4, [(0, 1, 4), (1, 2, -6), (2, 3, 5), (3, 1, -2)], 0, None),  # negative cycle
        (
            4,
            [(0, 1, 2), (2, 3, -1), (3, 2, -1)],
            0,
            [0, 2, None, None],
        ),  # cycle unreachable
        (1, [], 0, [0]),
    ],
)
def test_bellman_ford(n, edges, src, expected):
    assert bellman_ford(n, edges, src) == expected
