import pytest
from helpers import load

prim_mst = load("16_graphs.12_prim_mst").prim_mst


GFG_9 = [
    (0, 1, 4),
    (0, 7, 8),
    (1, 2, 8),
    (1, 7, 11),
    (2, 3, 7),
    (2, 8, 2),
    (2, 5, 4),
    (3, 4, 9),
    (3, 5, 14),
    (4, 5, 10),
    (5, 6, 2),
    (6, 7, 1),
    (6, 8, 6),
    (7, 8, 7),
]


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (9, GFG_9, 37),
        (4, [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)], 19),
        (3, [(0, 1, 5), (1, 2, 3), (0, 2, 1)], 4),
        (4, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1)], 3),  # ties
        (3, [(0, 1, -2), (1, 2, 3), (0, 2, 1)], -1),  # negative weight
        (2, [(0, 1, 7)], 7),
        (1, [], 0),
    ],
)
def test_prim_mst(n, edges, expected):
    assert prim_mst(n, edges) == expected
