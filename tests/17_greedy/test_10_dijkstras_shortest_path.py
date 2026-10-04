import pytest
from helpers import load

dijkstra = load("17_greedy.10_dijkstras_shortest_path").dijkstra

GFG_9 = [
    (0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2), (2, 5, 4),
    (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7),
]  # fmt: skip


@pytest.mark.parametrize(
    "n, edges, src, expected",
    [
        (3, [(0, 1, 1), (1, 2, 3), (0, 2, 6)], 2, [4, 3, 0]),
        (
            5,
            [(0, 1, 4), (0, 2, 8), (1, 4, 6), (2, 3, 2), (3, 4, 10)],
            0,
            [0, 4, 8, 10, 10],
        ),
        (9, GFG_9, 0, [0, 4, 12, 19, 21, 11, 9, 8, 14]),
        (4, [(0, 1, 0), (1, 2, 0), (2, 3, 5)], 3, [5, 5, 5, 0]),  # zero-weight edges
        (2, [(0, 1, 5), (0, 1, 2)], 1, [2, 0]),  # parallel edges
        (3, [(0, 1, 2)], 0, [0, 2, -1]),  # unreachable vertex
        (1, [], 0, [0]),
    ],
)
def test_dijkstra(n, edges, src, expected):
    assert dijkstra(n, edges, src) == expected
