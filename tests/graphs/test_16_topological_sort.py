import pytest
from helpers import load

topological_sort = load("graphs.16_topological_sort").topological_sort


@pytest.mark.parametrize(
    "n, edges",
    [
        (6, [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]),
        (4, [(0, 1), (0, 2), (1, 3), (2, 3)]),
        (4, [(3, 2), (2, 1), (1, 0)]),
        (5, [(0, 1), (2, 3)]),
        (3, []),
        (1, []),
    ],
)
def test_topological_sort_is_valid(n, edges):
    order = topological_sort(n, edges)
    assert sorted(order) == list(range(n))
    pos = {v: i for i, v in enumerate(order)}
    assert all(pos[u] < pos[v] for u, v in edges)


def test_topological_sort_unique_order():
    assert topological_sort(4, [(3, 2), (2, 1), (1, 0)]) == [3, 2, 1, 0]
