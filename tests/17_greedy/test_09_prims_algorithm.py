import pytest
from helpers import load

prim_mst = load("17_greedy.09_prims_algorithm").prim_mst


@pytest.mark.parametrize(
    "graph, expected",
    [
        (
            [
                [0, 2, 0, 6, 0],
                [2, 0, 3, 8, 5],
                [0, 3, 0, 0, 7],
                [6, 8, 0, 0, 9],
                [0, 5, 7, 9, 0],
            ],
            16,
        ),
        (
            [
                [0, 10, 6, 5],
                [10, 0, 0, 15],
                [6, 0, 0, 4],
                [5, 15, 4, 0],
            ],
            19,
        ),
        ([[0, 5, 1], [5, 0, 3], [1, 3, 0]], 4),
        ([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 2),  # all equal weights
        ([[0, 3], [3, 0]], 3),
        ([[0]], 0),
        ([], 0),
    ],
)
def test_prim_mst(graph, expected):
    assert prim_mst(graph) == expected
