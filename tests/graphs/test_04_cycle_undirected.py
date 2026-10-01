import pytest
from helpers import load

has_cycle_undirected = load("graphs.04_cycle_undirected").has_cycle_undirected


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (4, [(0, 1), (1, 2), (2, 3)], False),
        (4, [(0, 1), (1, 2), (2, 0), (2, 3)], True),
        (4, [(0, 1), (1, 2), (2, 3), (3, 0)], True),
        (5, [(0, 1), (2, 3), (3, 4), (4, 2)], True),  # cycle in a second component
        (4, [(0, 1), (0, 2), (0, 3)], False),  # star
        (6, [(0, 1), (2, 3), (4, 5)], False),
        (3, [], False),
        (1, [], False),
    ],
)
def test_has_cycle_undirected(n, edges, expected):
    assert has_cycle_undirected(n, edges) is expected
