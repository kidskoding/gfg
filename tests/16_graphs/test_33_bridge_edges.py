import pytest
from helpers import load

find_bridges = load("16_graphs.33_bridge_edges").find_bridges


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (5, [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)], [(0, 3), (3, 4)]),
        (6, [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 5), (5, 3)], [(2, 3)]),
        (4, [(0, 1), (1, 2), (2, 3)], [(0, 1), (1, 2), (2, 3)]),
        (3, [(0, 1), (1, 2), (2, 0)], []),
        (5, [(0, 1), (2, 3), (3, 4), (4, 2)], [(0, 1)]),  # disconnected
        (2, [(1, 0)], [(0, 1)]),
        (2, [], []),
    ],
)
def test_find_bridges(n, edges, expected):
    assert find_bridges(n, edges) == expected
