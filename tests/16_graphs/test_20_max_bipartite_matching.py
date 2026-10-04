import pytest
from helpers import load

max_bipartite_matching = load("16_graphs.20_max_bipartite_matching").max_bipartite_matching


@pytest.mark.parametrize(
    "bp_graph, expected",
    [
        (
            [
                [0, 1, 1, 0, 0, 0],
                [1, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1],
            ],
            5,
        ),
        ([[1, 1], [1, 0]], 2),  # greedy first-choice would block applicant 1
        ([[1, 1], [1, 1]], 2),
        ([[1, 0], [1, 0]], 1),
        ([[1, 1, 1]], 1),
        ([[1], [1], [1]], 1),
        ([[0, 0], [0, 0]], 0),
        ([[1]], 1),
    ],
)
def test_max_bipartite_matching(bp_graph, expected):
    assert max_bipartite_matching(bp_graph) == expected
