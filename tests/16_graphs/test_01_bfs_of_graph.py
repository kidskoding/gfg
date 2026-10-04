import pytest
from helpers import load

bfs_of_graph = load("16_graphs.01_bfs_of_graph").bfs_of_graph


@pytest.mark.parametrize(
    "adj, expected",
    [
        ([[2, 3, 1], [0], [0, 4], [0], [2]], [0, 2, 3, 1, 4]),
        ([[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]], [0, 1, 2, 3, 4]),
        ([[3, 1], [0], [3], [0, 2]], [0, 3, 1, 2]),  # neighbour order matters
        ([[1, 2], [3], [], []], [0, 1, 2, 3]),  # level by level, not depth first
        ([[1], [2], [3], []], [0, 1, 2, 3]),
        ([[1], [0], []], [0, 1]),  # vertex 2 unreachable
        ([[]], [0]),
    ],
)
def test_bfs_of_graph(adj, expected):
    assert bfs_of_graph(adj) == expected
