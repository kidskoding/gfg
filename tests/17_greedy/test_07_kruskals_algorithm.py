from collections import Counter

import pytest
from helpers import load

kruskal_mst = load("17_greedy.07_kruskals_algorithm").kruskal_mst


def _spans(n, edges):
    parent = list(range(n))

    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for u, v, _ in edges:
        parent[root(u)] = root(v)
    return len({root(x) for x in range(n)}) <= 1


@pytest.mark.parametrize(
    "n, edges, expected_weight",
    [
        (4, [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)], 19),
        (
            5,
            [
                (0, 1, 2),
                (0, 3, 6),
                (1, 2, 3),
                (1, 3, 8),
                (1, 4, 5),
                (2, 4, 7),
                (3, 4, 9),
            ],
            16,
        ),
        (3, [(0, 1, 5), (1, 2, 3), (0, 2, 1)], 4),
        (4, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1), (0, 2, 1)], 3),  # many MSTs
        (2, [(0, 1, 7), (0, 1, 3), (1, 1, 1)], 3),  # parallel edges + self loop
        (3, [(0, 1, -2), (1, 2, -3), (0, 2, 4)], -5),  # negative weights
        (1, [], 0),
    ],
)
def test_kruskal_mst(n, edges, expected_weight):
    mst = [tuple(e) for e in kruskal_mst(n, edges)]
    assert len(mst) == n - 1
    assert not Counter(mst) - Counter(
        edges
    )  # only input edges, no repeats beyond input
    assert _spans(n, mst)
    assert sum(w for _, _, w in mst) == expected_weight
