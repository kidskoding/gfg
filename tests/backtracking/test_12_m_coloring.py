import pytest
from helpers import load

graph_coloring = load("backtracking.12_m_coloring").graph_coloring

PETERSEN = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 0),
    (0, 5),
    (1, 6),
    (2, 7),
    (3, 8),
    (4, 9),
] + [
    (5, 7),
    (7, 9),
    (9, 6),
    (6, 8),
    (8, 5),
]


@pytest.mark.parametrize(
    "n, edges, m, expected",
    [
        (4, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)], 3, True),
        (3, [(0, 1), (1, 2), (0, 2)], 2, False),
        (4, [(0, 1), (1, 2), (2, 3), (3, 0)], 2, True),  # even cycle is bipartite
        (5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)], 2, False),  # odd cycle
        (4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)], 3, False),  # K4
        (10, PETERSEN, 3, True),
        (10, PETERSEN, 2, False),
        (3, [], 1, True),  # no edges
    ],
)
def test_graph_coloring(n, edges, m, expected):
    assert graph_coloring(n, edges, m) is expected
