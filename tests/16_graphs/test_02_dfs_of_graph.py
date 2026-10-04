import pytest
from helpers import load

dfs_of_graph = load("16_graphs.02_dfs_of_graph").dfs_of_graph


@pytest.mark.parametrize(
    "adj, expected",
    [
        ([[2, 3, 1], [0], [0, 4], [0], [2]], [0, 2, 4, 3, 1]),
        ([[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]], [0, 1, 2, 3, 4]),
        ([[3, 1], [0], [3], [0, 2]], [0, 3, 2, 1]),
        ([[1, 2], [3], [], []], [0, 1, 3, 2]),  # depth first, not level by level
        ([[1], [0], []], [0, 1]),  # vertex 2 unreachable
        ([[]], [0]),
    ],
)
def test_dfs_of_graph(adj, expected):
    assert dfs_of_graph(adj) == expected
