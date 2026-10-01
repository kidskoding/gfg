import pytest
from helpers import load

kosaraju_scc = load("graphs.34_scc_kosaraju").kosaraju_scc


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (5, [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)], [[0, 1, 2], [3], [4]]),
        (
            8,
            [
                (0, 1),
                (1, 2),
                (2, 0),
                (2, 3),
                (3, 4),
                (4, 7),
                (4, 5),
                (5, 6),
                (6, 4),
                (6, 7),
            ],
            [[0, 1, 2], [3], [4, 5, 6], [7]],
        ),
        (
            6,
            [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 5), (5, 3)],
            [[0, 1, 2], [3, 4, 5]],
        ),
        (4, [(0, 1), (1, 2), (2, 3), (3, 0)], [[0, 1, 2, 3]]),
        (2, [(0, 0), (0, 1)], [[0], [1]]),  # self-loop
        (3, [], [[0], [1], [2]]),
        (1, [], [[0]]),
    ],
)
def test_kosaraju_scc(n, edges, expected):
    assert sorted(sorted(c) for c in kosaraju_scc(n, edges)) == expected
