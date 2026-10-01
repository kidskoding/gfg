from itertools import pairwise

import pytest
from helpers import load

hamiltonian_cycle = load("backtracking.10_hamiltonian_cycle").hamiltonian_cycle


def _matrix(n, edges):
    g = [[0] * n for _ in range(n)]
    for u, v in edges:
        g[u][v] = g[v][u] = 1
    return g


PETERSEN = _matrix(
    10,
    [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
    + [(5, 7), (7, 9), (9, 6), (6, 8), (8, 5)],
)


@pytest.mark.parametrize(
    "graph",
    [
        [
            [0, 1, 0, 1, 0],
            [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0],
        ],
        _matrix(3, [(0, 1), (1, 2), (2, 0)]),
        _matrix(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]),
        _matrix(
            6, [(0, 3), (3, 1), (1, 4), (4, 2), (2, 5), (5, 0), (0, 1)]
        ),  # cycle with a chord
    ],
)
def test_hamiltonian_cycle_found(graph):
    cycle = hamiltonian_cycle(graph)
    n = len(graph)
    assert cycle is not None
    assert len(cycle) == n + 1
    assert cycle[0] == cycle[-1] == 0
    assert sorted(cycle[:-1]) == list(range(n))
    assert all(graph[a][b] for a, b in pairwise(cycle))


@pytest.mark.parametrize(
    "graph",
    [
        [
            [0, 1, 0, 1, 0],
            [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0],
        ],
        _matrix(4, [(0, 1), (1, 2), (2, 3)]),  # path graph
        _matrix(4, [(0, 1), (0, 2), (0, 3)]),  # star
        _matrix(4, [(0, 1), (1, 2), (2, 0)]),  # vertex 3 isolated
        PETERSEN,
    ],
)
def test_hamiltonian_cycle_none(graph):
    assert hamiltonian_cycle(graph) is None
