import pytest
from helpers import load

zero_one_bfs = load("08_deques.10_zero_one_bfs").zero_one_bfs

GFG_EDGES = [
    (0, 1, 0),
    (0, 7, 1),
    (1, 7, 1),
    (1, 2, 1),
    (2, 3, 0),
    (2, 5, 0),
    (2, 8, 1),
    (3, 4, 1),
    (3, 5, 1),
    (4, 5, 1),
    (5, 6, 1),
    (6, 7, 1),
    (7, 8, 1),
]


@pytest.mark.parametrize(
    "n, edges, src, expected",
    [
        (9, GFG_EDGES, 0, [0, 0, 1, 1, 2, 1, 2, 1, 2]),
        (4, [(0, 3, 1), (0, 1, 0), (1, 2, 1), (2, 3, 0)], 0, [0, 0, 1, 1]),
        (
            3,
            [(0, 2, 1), (0, 1, 0), (1, 2, 0)],
            0,
            [0, 0, 0],
        ),  # zero detour beats direct edge
        (4, [(0, 1, 0), (1, 2, 0), (2, 3, 0)], 3, [0, 0, 0, 0]),
        (4, [(0, 1, 1), (1, 2, 1), (2, 3, 1)], 2, [2, 1, 0, 1]),  # edges are undirected
        (2, [(0, 1, 1), (0, 1, 0)], 1, [0, 0]),  # parallel edges
        (3, [(0, 1, 1)], 0, [0, 1, -1]),  # unreachable
        (1, [], 0, [0]),
    ],
)
def test_zero_one_bfs(n, edges, src, expected):
    assert zero_one_bfs(n, edges, src) == expected
