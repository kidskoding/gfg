import pytest
from helpers import load

dial_shortest_paths = load("17_greedy.16_dials_algorithm").dial_shortest_paths

GFG_9 = [
    (0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2), (2, 5, 4),
    (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7),
]  # fmt: skip


@pytest.mark.parametrize(
    "n, edges, src, expected",
    [
        (9, GFG_9, 0, [0, 4, 12, 19, 21, 11, 9, 8, 14]),
        (4, [(0, 1, 5), (1, 2, 5), (0, 2, 9), (2, 3, 1)], 3, [10, 6, 1, 0]),
        (
            5,
            [(0, 1, 100), (0, 2, 1), (2, 3, 1), (3, 1, 1), (1, 4, 100)],
            0,
            [0, 3, 1, 2, 103],
        ),
        (3, [(0, 1, 0), (1, 2, 0)], 0, [0, 0, 0]),  # zero-weight edges
        (4, [(0, 1, 1)], 0, [0, 1, -1, -1]),  # unreachable vertices
        (1, [], 0, [0]),
    ],
)
def test_dial_shortest_paths(n, edges, src, expected):
    assert dial_shortest_paths(n, edges, src) == expected
