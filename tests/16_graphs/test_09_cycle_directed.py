import pytest
from helpers import load

has_cycle_directed = load("16_graphs.09_cycle_directed").has_cycle_directed


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (4, [(0, 1), (1, 2), (2, 3)], False),
        (4, [(0, 1), (1, 2), (2, 0), (2, 3)], True),
        (3, [(0, 1), (0, 2), (1, 2)], False),  # undirected triangle, but a DAG
        (2, [(0, 1), (1, 0)], True),
        (1, [(0, 0)], True),  # self-loop
        (5, [(0, 1), (3, 4), (4, 2), (2, 3)], True),  # cycle away from vertex 0
        (4, [(0, 1), (0, 2), (1, 3), (2, 3)], False),  # diamond
        (3, [], False),
    ],
)
def test_has_cycle_directed(n, edges, expected):
    assert has_cycle_directed(n, edges) is expected
