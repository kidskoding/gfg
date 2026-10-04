import pytest
from helpers import load

dijkstra = load("14_heaps.29_dijkstra_shortest_paths").dijkstra


@pytest.mark.parametrize(
    "n, edges, src, expected",
    [
        (3, [(0, 1, 1), (1, 2, 3), (0, 2, 6)], 2, [4, 3, 0]),
        (4, [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)], 0, [0, 3, 1, 4]),
        (3, [(0, 1, 5)], 0, [0, 5, -1]),  # node 2 unreachable
        (2, [(0, 1, 7), (1, 0, 2)], 1, [2, 0]),  # parallel edges
        (2, [(0, 1, 0)], 0, [0, 0]),  # zero-weight edge
        (1, [], 0, [0]),
    ],
)
def test_dijkstra(n, edges, src, expected):
    assert dijkstra(n, edges, src) == expected
