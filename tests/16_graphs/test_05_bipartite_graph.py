import pytest
from helpers import load

is_bipartite = load("16_graphs.05_bipartite_graph").is_bipartite


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (4, [(0, 1), (1, 2), (2, 3), (3, 0)], True),  # even cycle
        (3, [(0, 1), (1, 2), (2, 0)], False),  # triangle
        (5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)], False),  # odd cycle
        (4, [(0, 1), (0, 2), (0, 3)], True),
        (6, [(0, 1), (1, 2), (3, 4), (4, 5)], True),
        (6, [(0, 1), (2, 3), (3, 4), (4, 2)], False),  # odd cycle in another component
        (1, [], True),
        (3, [], True),
    ],
)
def test_is_bipartite(n, edges, expected):
    assert is_bipartite(n, edges) is expected
